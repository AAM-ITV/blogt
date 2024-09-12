#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from prometheus_client import start_http_server, Summary # type: ignore


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_blog.settings')
    
     # Запускаем HTTP-сервер для сбора метрик Prometheus на порту 8000
    start_http_server(8080)

    try:
        from django.core.management import execute_from_command_line # type: ignore
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
