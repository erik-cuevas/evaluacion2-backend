"""Compat shim: export models/views from the new app to keep legacy imports working.

Este archivo permite que imports como `from market.models import Producto`
siguan funcionando redirigiéndolos a `gestionador_productos`.
"""

from gestionador_productos import models as _gp_models

# Expose Producto at market.models.Producto
Producto = _gp_models.Producto
