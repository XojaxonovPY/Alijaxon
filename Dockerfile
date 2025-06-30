# Python image
FROM python:3.10-slim

# Ishchi papkani yaratamiz
WORKDIR /app

# Kutubxonalarni o'rnatamiz
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Loyiha fayllarini nusxalaymiz
COPY . .

# Static fayllarni yig'amiz
RUN python manage.py collectstatic --noinput

# Django serverni ishga tushiramiz
CMD ["gunicorn", "root.wsgi:application", "--bind", "0.0.0.0:8000"]
