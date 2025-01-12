# Сайт доставки еды Star Burger

Это сайт сети ресторанов Star Burger. Здесь можно заказать превосходные бургеры с доставкой на дом.

![скриншот сайта](https://dvmn.org/filer/canonical/1594651635/686/)


Сеть Star Burger объединяет несколько ресторанов, действующих под единой франшизой. У всех ресторанов одинаковое меню и одинаковые цены. Просто выберите блюдо из меню на сайте и укажите место доставки. Мы сами найдём ближайший к вам ресторан, всё приготовим и привезём.

На сайте есть три независимых интерфейса. Первый — это публичная часть, где можно выбрать блюда из меню, и быстро оформить заказ без регистрации и SMS.

Второй интерфейс предназначен для менеджера. Здесь происходит обработка заказов. Менеджер видит поступившие новые заказы и первым делом созванивается с клиентом, чтобы подтвердить заказ. После оператор выбирает ближайший ресторан и передаёт туда заказ на исполнение. Там всё приготовят и сами доставят еду клиенту.

Третий интерфейс — это админка. Преимущественно им пользуются программисты при разработке сайта. Также сюда заходит менеджер, чтобы обновить меню ресторанов Star Burger.

## Как запустить dev-версию сайта

Для запуска сайта нужно запустить **одновременно** бэкенд и фронтенд, в двух терминалах.

### Как собрать бэкенд

Скачайте код:
```sh
git clone https://github.com/devmanorg/star-burger.git
```

Перейдите в каталог проекта:
```sh
cd star-burger
```

[Установите Python](https://www.python.org/), если этого ещё не сделали.

Проверьте, что `python` установлен и корректно настроен. Запустите его в командной строке:
```sh
python --version
```
**Важно!** Версия Python должна быть не ниже 3.6.

Возможно, вместо команды `python` здесь и в остальных инструкциях этого README придётся использовать `python3`. Зависит это от операционной системы и от того, установлен ли у вас Python старой второй версии.

В каталоге проекта создайте виртуальное окружение:
```sh
python -m venv venv
```
Активируйте его. На разных операционных системах это делается разными командами:

- Windows: `.\venv\Scripts\activate`
- MacOS/Linux: `source venv/bin/activate`


Установите зависимости в виртуальное окружение:
```sh
pip install -r requirements.txt
```

Определите переменную окружения `SECRET_KEY`. Создать файл `.env` в каталоге `star_burger/` и положите туда такой код:
```sh
SECRET_KEY=django-insecure-0if40nf4nf93n4
```

Создайте файл базы данных SQLite и отмигрируйте её следующей командой:

```sh
python manage.py migrate
```

Запустите сервер:

```sh
python manage.py runserver
```

Откройте сайт в браузере по адресу [http://127.0.0.1:8000/](http://127.0.0.1:8000/). Если вы увидели пустую белую страницу, то не пугайтесь, выдохните. Просто фронтенд пока ещё не собран. Переходите к следующему разделу README.

### Собрать фронтенд

**Откройте новый терминал**. Для работы сайта в dev-режиме необходима одновременная работа сразу двух программ `runserver` и `parcel`. Каждая требует себе отдельного терминала. Чтобы не выключать `runserver` откройте для фронтенда новый терминал и все нижеследующие инструкции выполняйте там.

[Установите Node.js](https://nodejs.org/en/), если у вас его ещё нет.

Проверьте, что Node.js и его пакетный менеджер корректно установлены. Если всё исправно, то терминал выведет их версии:

```sh
nodejs --version
# v16.16.0
# Если ошибка, попробуйте node:
node --version
# v16.16.0

npm --version
# 8.11.0
```

Версия `nodejs` должна быть не младше `10.0` и не старше `16.16`. Лучше ставьте `16.16.0`, её мы тестировали. Версия `npm` не важна. Как обновить Node.js читайте в статье: [How to Update Node.js](https://phoenixnap.com/kb/update-node-js-version).

Перейдите в каталог проекта и установите пакеты Node.js:

```sh
cd star-burger
npm ci --dev
```

Команда `npm ci` создаст каталог `node_modules` и установит туда пакеты Node.js. Получится аналог виртуального окружения как для Python, но для Node.js.

Помимо прочего будет установлен [Parcel](https://parceljs.org/) — это упаковщик веб-приложений, похожий на [Webpack](https://webpack.js.org/). В отличии от Webpack он прост в использовании и совсем не требует настроек.

Теперь запустите сборку фронтенда и не выключайте. Parcel будет работать в фоне и следить за изменениями в JS-коде:

```sh
./node_modules/.bin/parcel watch bundles-src/index.js --dist-dir bundles --public-url="./"
```

Если вы на Windows, то вам нужна та же команда, только с другими слешами в путях:

```sh
.\node_modules\.bin\parcel watch bundles-src/index.js --dist-dir bundles --public-url="./"
```

Дождитесь завершения первичной сборки. Это вполне может занять 10 и более секунд. О готовности вы узнаете по сообщению в консоли:

```
✨  Built in 10.89s
```

Parcel будет следить за файлами в каталоге `bundles-src`. Сначала он прочитает содержимое `index.js` и узнает какие другие файлы он импортирует. Затем Parcel перейдёт в каждый из этих подключенных файлов и узнает что импортируют они. И так далее, пока не закончатся файлы. В итоге Parcel получит полный список зависимостей. Дальше он соберёт все эти сотни мелких файлов в большие бандлы `bundles/index.js` и `bundles/index.css`. Они полностью самодостаточно и потому пригодны для запуска в браузере. Именно эти бандлы сервер отправит клиенту.

Теперь если зайти на страницу  [http://127.0.0.1:8000/](http://127.0.0.1:8000/), то вместо пустой страницы вы увидите:

![](https://dvmn.org/filer/canonical/1594651900/687/)

Каталог `bundles` в репозитории особенный — туда Parcel складывает результаты своей работы. Эта директория предназначена исключительно для результатов сборки фронтенда и потому исключёна из репозитория с помощью `.gitignore`.

**Сбросьте кэш браузера <kbd>Ctrl-F5</kbd>.** Браузер при любой возможности старается кэшировать файлы статики: CSS, картинки и js-код. Порой это приводит к странному поведению сайта, когда код уже давно изменился, но браузер этого не замечает и продолжает использовать старую закэшированную версию. В норме Parcel решает эту проблему самостоятельно. Он следит за пересборкой фронтенда и предупреждает JS-код в браузере о необходимости подтянуть свежий код. Но если вдруг что-то у вас идёт не так, то начните ремонт со сброса браузерного кэша, жмите <kbd>Ctrl-F5</kbd>.


## Как запустить prod-версию сайта

Собрать фронтенд:

```sh
./node_modules/.bin/parcel build bundles-src/index.js --dist-dir bundles --public-url="./"
```

Настроить бэкенд: создать файл `.env` в каталоге `star_burger/` со следующими настройками:

- `DEBUG` — дебаг-режим. Поставьте `False`.
- `SECRET_KEY` — секретный ключ проекта. Он отвечает за шифрование на сайте. Например, им зашифрованы все пароли на вашем сайте.
- `ALLOWED_HOSTS` — [см. документацию Django](https://docs.djangoproject.com/en/3.1/ref/settings/#allowed-hosts)
- `YANDEX_GEOCODER_API_KEY` — [см. статью](https://dvmn.org/encyclopedia/api-docs/yandex-geocoder-api/)
- `DATABASE_URL` — настройки доступа к базе данных PostgreSQL с помощью одного URL,
пример URL для PostgreSQL может выглядеть следующим образом:
`postgres://имя_пользователя:пароль@localhost:5432/имя_базы_данных`.
Вы можете указать соответствующие значения для имени пользователя, пароля, хоста и имени базы данных в URL.
- `ROLLBAR_ACCESS_TOKEN` — необязательный параметр. Токен для [Rollbar](https://rollbar.com/) — сервиса для сбора ошибок. Если вы не хотите использовать Rollbar, то просто удалите эту строку из файла `.env`.

Создать базу данных PostgreSQL и пользователя к ней:

```sh
sudo -u postgres psql
```

```sql
CREATE DATABASE new_db_name WITH ENCODING='UTF8' LC_CTYPE='ru_RU.UTF-8' LC_COLLATE='ru_RU.UTF-8' OWNER=postgres TEMPLATE=template0;
GRANT ALL PRIVILEGES ON DATABASE star_burger_db TO postgres;
ALTER USER username WITH PASSWORD 'new_password';
```

Создайте файл star_burger.service в каталоге /etc/systemd/system со следующим содержимым:

```sh
[Unit]
Requires=postgresql.service
After=postgresql.service
[Service]
WorkingDirectory=/opt/star-burger
ExecStart=/opt/star-burger/env/bin/gunicorn -w 3 --bind 127.0.0.1:8000 star_burger.wsgi:application
Restart=always
[Install]
WantedBy=multi-user.target
```
Также необходимо настроить файлы обновления сертификатов SSL. Для этого создайте файл certbot-renewal.service и certbot-renewal.timer в каталоге /etc/systemd/system со следующим содержимым:

certbot-renewal
```sh
[Unit]
Description=Certbot Renewal

[Service]
ExecStart=/usr/bin/certbot renew --force-renewal --post-hook "systemctl reload nginx.service"
```

certbot-renewal.timer
```sh
[Unit]
Description=Timer for Certbot Renewal

[Timer]
OnBootSec=300
OnUnitActiveSec=1w

[Install]
WantedBy=multi-user.target
```
Настройка для очистки сессий. Создайте файл starburger-clearsessions.service и starburger-clearsessions.timer в каталоге /etc/systemd/system со следующим содержимым:

```sh
[Unit]
Description=Clear Django Sessions
Requires=star_burger.service
[Service]
WorkingDirectory=/opt/star-burger
ExecStart=/opt/star-burger/env/bin/python3 manage.py clearsessions
Restart=on-abort
[Install]
WantedBy=multi-user.target
```

```sh
[Unit]
Description=Timer for Clearsessions

[Timer]
OnBootSec=300
OnUnitActiveSec=1w

[Install]
WantedBy=multi-user.target
```
Далее следует добавить сервисы в автозагрузку:

```sh
sudo systemctl daemon-reload
sudo systemctl enable star_burger
sudo systemctl enable certbot-renewal.timer
sudo systemctl enable starburger-clearsessions.timer
```

Настроить nginx: создать файл `/etc/nginx/sites-enabled/starbrger` со следующим содержимым:

```sh
server {
    server_name kek.lolkekazaza.ru, www.kek.lolkekazaza.ru; # managed by Certbot

    location / {
        include proxy_params;
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
    location /static/ {
        alias /opt/star-burger/static/;
    }
    location /media/ {
        alias /opt/star-burger/media/;
    }



    listen 443 ssl; # managed by Certbot
    ssl_certificate /etc/letsencrypt/live/www.kek.lolkekazaza.ru/fullchain.pem; # managed by Certbot
    ssl_certificate_key /etc/letsencrypt/live/www.kek.lolkekazaza.ru/privkey.pem; # managed by Certbot
    include /etc/letsencrypt/options-ssl-nginx.conf; # managed by Certbot
    ssl_dhparam /etc/letsencrypt/ssl-dhparams.pem; # managed by Certbot

}
server {
    if ($host = kek.lolkekazaza.ru) {
        return 301 https://$host$request_uri;
    } # managed by Certbot
    if ($host = www.kek.lolkekazaza.ru) {
        return 301 https://$host$request_uri;
    }
    listen 80;
    server_name kek.lolkekazaza.ru www.kek.lolkekazaza.ru;
    return 404;
}
```

Перезапустите nginx:

```sh
sudo systemctl restart nginx
```

При необходимости внесения изменений в репозиторий, можно обновить проект с помощью скрипта `script_star_burger`, который находится в корне проекта:


```sh
./script_star_burger
```
Ссылка на демонстрационную версию проекта: [kek.lolkekazaza.ru](https://kek.lolkekazaza.ru/)


## Как запустить dev-версию сайта через Docker

Установите [Docker](https://docs.docker.com/engine/install/) и [Docker Compose](https://docs.docker.com/compose/install/).

У вас также должны быть получены сертификаты SSL для домена на котором будет запущен сайт и создана база данных Postgres. Смотри раздел [Как запустить prod-версию сайта](#как-запустить-prod-версию-сайта).

Склонируйте репозиторий:

```sh
git clone https://github.com/devmanorg/star-burger.git
```

Настойте переменные окружения в файле `.env` в корне проекта, смотри раздел [Как запустить prod-версию сайта](#как-запустить-prod-версию-сайта).

Запустите скрипт `script_star_burger_with_docker_compose.sh` в корне проекта:

```sh
./script_star_burger_with_docker_compose.sh
```

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org). За основу был взят код проекта [FoodCart](https://github.com/Saibharath79/FoodCart).

Где используется репозиторий:

- Второй и третий урок [учебного курса Django](https://dvmn.org/modules/django/)
