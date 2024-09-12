FROM python:3.9-slim

WORKDIR /app

COPY . /app

# Устанавливаем зависимости
RUN pip install --upgrade pip
RUN pip install Django==2.2.7 django-crispy-forms Pillow
RUN pip install prometheus_client

# Применяем миграции
RUN python manage.py makemigrations
RUN python manage.py migrate

# Открываем порт для доступа
EXPOSE 8000

# Запускаем приложение
CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]
