# Generated by Django 4.2.4 on 2023-11-10 04:17

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre de la categoria')),
                ('imagen', models.CharField(max_length=2000, verbose_name='Dirección de la imagen')),
                ('creado', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
                'db_table': 'categoria',
            },
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150, verbose_name='Nombre de la marca')),
                ('imagen', models.CharField(max_length=2000, verbose_name='Ruta de la imagen')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre de la categoria')),
                ('precio', models.PositiveIntegerField(default=40000, verbose_name='precio')),
                ('disponibilidad', models.CharField(choices=[('a', 'Arrendado'), ('g', 'Agotado'), ('s', 'En stock')], default='s', max_length=1)),
                ('cantidad', models.PositiveIntegerField(max_length=2, verbose_name='Cantidad')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='Inventario.categoria')),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
                'db_table': 'productos',
            },
        ),
    ]
