import phonenumbers
from django.http import JsonResponse
from django.templatetags.static import static
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Product, Order, OrderItem


def banners_list_api(request):
    # FIXME move data to db?
    return JsonResponse([
        {
            'title': 'Burger',
            'src': static('burger.jpg'),
            'text': 'Tasty Burger at your door step',
        },
        {
            'title': 'Spices',
            'src': static('food.jpg'),
            'text': 'All Cuisines',
        },
        {
            'title': 'New York',
            'src': static('tasty.jpg'),
            'text': 'Food is incomplete without a tasty dessert',
        }
    ], safe=False, json_dumps_params={
        'ensure_ascii': False,
        'indent': 4,
    })


def product_list_api(request):
    products = Product.objects.select_related('category').available()

    dumped_products = []
    for product in products:
        dumped_product = {
            'id': product.id,
            'name': product.name,
            'price': product.price,
            'special_status': product.special_status,
            'description': product.description,
            'category': {
                'id': product.category.id,
                'name': product.category.name,
            } if product.category else None,
            'image': product.image.url,
            'restaurant': {
                'id': product.id,
                'name': product.name,
            }
        }
        dumped_products.append(dumped_product)
    return JsonResponse(dumped_products, safe=False, json_dumps_params={
        'ensure_ascii': False,
        'indent': 4,
    })


@api_view(['POST'])
def register_order(request):
    order_info = request.data
    product_ids = Product.objects.values_list('id', flat=True)
    keys_to_check = ['products', 'firstname', 'lastname', 'phonenumber', 'address']
    print(order_info)
    print(product_ids)

    missing_keys = [key for key in keys_to_check if key not in order_info]
    print(missing_keys)
    if missing_keys:
        return Response({'error': f'Отсутствуют обязательные ключи: {", ".join(missing_keys)}'}, status=400)

    if not isinstance(order_info['products'], list) or not order_info['products']:
        return Response({'error': 'Список продуктов пуст'}, status=400)

    for product in order_info['products']:
        if product["product"] not in product_ids:
            return Response({'error': f'Продукт с id {product["product"]} не найден'}, status=400)

    not_str_fields = [key for key, value in order_info.items() if key != 'products' and not isinstance(value, str)]
    if not_str_fields:
        return Response({'error': f'fields {", ".join(not_str_fields)} is not a string'}, status=400)

    empty_fields = [key for key, value in order_info.items() if not value]
    if empty_fields:
        return Response({'error': f'fields {", ".join(empty_fields)} is empty'}, status=400)

    parse_number = phonenumbers.parse(order_info['phonenumber'], "RU")
    if not phonenumbers.is_valid_number(parse_number):
        return Response({'error': f'Невалидный номер телефона'}, status=400)

    order = Order.objects.create(
        name=order_info['firstname'],
        given_name=order_info['lastname'],
        phone=order_info['phonenumber'],
        address=order_info['address'],
    )

    for products in order_info['products']:
        order_items = OrderItem.objects.create(
            product_id=products['product'],
            quantity=products['quantity'],
            order=order,
        )
    return Response({'order_id': order.id}, status=201)
