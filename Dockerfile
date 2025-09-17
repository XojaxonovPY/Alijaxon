FROM python:3.13-alpine

WORKDIR /app
COPY . .

RUN pip install -r requirements.txt

CMD ["/bin/sh", "-c", "\
    python manage.py migrate --noinput && \
    python manage.py loaddata user.json adminsetting.json products.json categories.json regions.json disdricts.json && \
    python manage.py runserver 0.0.0.0:8002 \
"]
