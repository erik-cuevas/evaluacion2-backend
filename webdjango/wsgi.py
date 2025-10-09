"""WSGI config para el proyecto webdjango.

Este archivo expone la aplicación WSGI mediante la variable `application`.
Se utiliza en despliegues tradicionales con servidores WSGI (por ejemplo
Gunicorn, uWSGI) en producción.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'webdjango.settings')

application = get_wsgi_application()
