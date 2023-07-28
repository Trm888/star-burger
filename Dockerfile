FROM python:3.11

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /star-burger

COPY requirements.txt .

RUN pip install -r requirements.txt
RUN pip install gunicorn

COPY . .

ENV DJANGO_SETTINGS_MODULE=star_burger.settings

CMD []
