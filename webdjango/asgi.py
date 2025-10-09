"""ASGI config para el proyecto webdjango.

Este archivo expone la aplicación ASGI mediante la variable `application`.
Se utiliza en despliegues asíncronos o cuando se trabaja con servidores
compatibles con ASGI. Para despliegue tradicional WSGI se usa `wsgi.py`.
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'webdjango.settings')

application = get_asgi_application()
