# Generated by Django 3.2.23 on 2023-12-03 14:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Inventario', '0010_auto_20231125_1554'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='categoria',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.RESTRICT, to='Inventario.categoria'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='marca',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.RESTRICT, to='Inventario.marca'),
        ),
    ]