from rest_framework import serializers
from Inventario.models import Categoria, Marca, Producto

class ProductoSerializar(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'

class CategoriaSerializar(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class MarcaSerializar(serializers.ModelSerializer):
    class Meta:
        model = Marca
        fields = '__all__'