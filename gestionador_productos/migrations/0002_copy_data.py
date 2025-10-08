from django.db import migrations


def copy_market_to_gestionador(apps, schema_editor):
    # Use historical models to avoid import-time issues
    # Attempt to get the old model; if the 'market' app isn't installed
    # (e.g., after consolidation), simply skip the copy to avoid failing
    # migrations in fresh environments.
    try:
        MarketProducto = apps.get_model('market', 'Producto')
    except LookupError:
        # Nothing to copy from; the environment doesn't have the old app.
        return

    GestionProducto = apps.get_model('gestionador_productos', 'Producto')

    db_alias = schema_editor.connection.alias

    for old in MarketProducto.objects.using(db_alias).all():
        # Create a new object in the new table with same field values
        GestionProducto.objects.using(db_alias).create(
            nombre=old.nombre,
            descripcion=old.descripcion,
            precio=old.precio,
            imagen=old.imagen.name if old.imagen else None,
            created_at=old.created_at,
        )


class Migration(migrations.Migration):

    dependencies = [
        ('gestionador_productos', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(copy_market_to_gestionador, reverse_code=migrations.RunPython.noop),
    ]
