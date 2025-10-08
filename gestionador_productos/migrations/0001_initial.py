# Generated manual migration to create Producto model table for gestionador_productos
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    # No external dependencies: this migration creates the new table for
    # gestionador_productos. The previous data copy was executed earlier.
    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField(blank=True)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=8)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='productos/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
            },
        ),
    ]
