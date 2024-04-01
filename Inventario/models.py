import email
from tabnanny import verbose
from django.db import models
from django.utils import timezone
from Inventario.choices import disponibilidades

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=100,verbose_name='Nombre de la categoria')
    imagen = models.CharField(max_length=2000, blank=True, verbose_name="Dirección de la imagen")
    descripcion = models.CharField(max_length=3000, verbose_name="Descripción", default='Descripción de la categoria')

    def __str__(self):
        return "{}".format(self.nombre)
    
    class Meta:
        db_table = "categorias"
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

class Marca(models.Model):
    nombre = models.CharField(max_length=150, verbose_name="Nombre de la marca")
    imagen = models.CharField(max_length=2000, blank=True, verbose_name="Ruta de la imagen")
    descripcion = models.CharField(max_length=3000, verbose_name='Descripción', default='Descripción de la marca')

    def __str__(self) -> str:
        return "{}".format(self.nombre)

    class Meta:
        db_table = "marcas"
        verbose_name = "Marca"    
        verbose_name_plural = "Marcas"

class Producto(models.Model):
    nombre = models.CharField(max_length=100,verbose_name='Nombre de la categoria')
    categoria = models.ForeignKey(Categoria, null=True, on_delete=models.RESTRICT, default=1)
    marca = models.ForeignKey(Marca, null=True, on_delete=models.RESTRICT, default=1)
    precio = models.PositiveIntegerField(default=40000, verbose_name="precio")
    disponibilidad = models.CharField(max_length=1, choices= disponibilidades, default='s')
    cantidad = models.PositiveIntegerField(verbose_name="Cantidad")
    imagen = models.CharField(max_length=2000, verbose_name="Dirección de la imagen", blank=True)

    def __str__(self):
        return "{}: {} unidades".format(self.nombre, self.cantidad)
    
    class Meta:
        db_table = "productos"
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

