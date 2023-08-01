FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update \
    && apt-get install -y gcc libpq-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /star-burger

COPY requirements.txt .

RUN pip install --upgrade pip && pip install -r requirements.txt && pip install gunicorn

RUN chmod -R 777 /star-burger

COPY . .

ENV DJANGO_SETTINGS_MODULE=star_burger.settings

CMD ["gunicorn","--bind","0.0.0.0:8000","star_burger.wsgi:application"]
