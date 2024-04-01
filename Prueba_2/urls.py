"""
URL configuration for Prueba_2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from Prueba_API import views as apis
from Inventario import views as vistas

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', vistas.entrance, name="Home"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register', vistas.añadir_usuario, name='register'),

    path('productosAPI/', apis.productosAPI, name='productosAPI'),
    path('productosListaAPI/', apis.producto_listado, name='productosListAPI'),
    path('productosListaAPI/<int:pk>', apis.producto_detalle, name='productosDetailAPI'),

    path('categoriasAPI/', apis.categoriasAPI, name='categoriasAPI'),
    path('categoriasListaAPI/', apis.categoria_listado, name='categoriasListAPI'),
    path('categoriasListaAPI/<int:pk>', apis.categoria_detalle, name='categoriasDetailAPI'),

    path('marcasAPI/', apis.marcasAPI, name='marcasAPI'),
    path('marcasListaAPI/', apis.marca_listado, name='marcasListAPI'),
    path('marcasListaAPI/<int:pk>', apis.marca_detalle, name='marcasDetailAPI'),

    path('Home/', vistas.Home, name='Select'),
    path('verMarcas/', vistas.ver_marcas, name='Detalles_marcas'),
    path('verCategorias/', vistas.ver_categorias, name='Detalles_categorias'),
    path('Categorias/<int:nombre_set>', vistas.ver_productos, name="Detalles_categoria"),

    path('AñadirMarca/',vistas.añadir_marca, name='añadirMarca'),
    path('marcaEdit/<int:marca_id>', vistas.cargar_editar_marca, name="editarMarca"),
    path('marcaEditado/<int:marca_id>', vistas.editar_marca, name="marcaEditado"),
    path('marcaDel/<int:marca_id>', vistas.eliminar_marca, name='eliminarMarca'),

    path('AñadirCategoria/',vistas.añadir_categoria, name='añadirCategoria'),
    path('categoriaEdit/<int:categoria_id>', vistas.cargar_editar_categoria, name="editarCategoria"),
    path('categoriaEditado/<int:categoria_id>', vistas.editar_categoria, name="categoriaEditado"),
    path('categoriaDel/<int:categoria_id>', vistas.eliminar_categoria, name='eliminarCategoria'),

    path('AñadirProducto/',vistas.añadir_producto, name='añadirProducto'),
    path('productoEdit/<int:producto_id>', vistas.cargar_editar_producto, name="editarProducto"),
    path('productoEditado/<int:producto_id>', vistas.editar_producto, name="productoEditado"),
    path('productoDel/<int:producto_id>', vistas.eliminar_producto, name='eliminarProducto')
]
