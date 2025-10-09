#!/usr/bin/env python
"""Entrada de comandos para el proyecto Django.

Este script se usa para ejecutar comandos como `runserver`, `migrate` y
`test`. Se mantiene igual que el original generado por Django pero con
este docstring en español para aclarar su propósito.
"""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'webdjango.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
