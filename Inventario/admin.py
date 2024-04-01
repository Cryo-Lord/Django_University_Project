from django.contrib import admin
from Inventario.models import Categoria,Marca,Producto

class MarcaAdmin(admin.ModelAdmin):
    list_display = ['nombre','imagen', 'descripcion']

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nombre','imagen','descripcion']

class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre','precio','disponibilidad','cantidad','categoria','imagen']

admin.site.register(Marca, MarcaAdmin)
admin.site.register(Categoria,CategoriaAdmin)
admin.site.register(Producto, ProductoAdmin)