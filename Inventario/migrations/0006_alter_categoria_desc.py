# Generated by Django 4.2.4 on 2023-11-12 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inventario', '0005_remove_categoria_creado_categoria_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='desc',
            field=models.CharField(default='Descripción de la categoria', max_length=3000, verbose_name='Descripción'),
        ),
    ]
