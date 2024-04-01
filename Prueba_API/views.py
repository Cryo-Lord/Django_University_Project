from django.shortcuts import render
from django.http import JsonResponse
from Prueba_API.serializers import ProductoSerializar, MarcaSerializar, CategoriaSerializar
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from Inventario.models import Producto, Categoria, Marca

# Create your views here.
def productosAPI(request):
    productos = Producto.objects.all()
    serializer = ProductoSerializar(productos, many=True)
    return Response(serializer.data)

def categoriasAPI(request):
    categorias = Categoria.objects.all()
    serializer = CategoriaSerializar(categorias, many=True)
    return Response(serializer.data)

def marcasAPI(request):
    marcas = Marca.objects.all()
    serializer = MarcaSerializar(marcas, many=True)
    return Response(serializer.data)

@api_view(['GET','POST'])
def producto_listado(request):
    if request.method == 'GET':
        productos = Producto.objects.all()
        serializer = ProductoSerializar(productos, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = ProductoSerializar(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','POST'])
def categoria_listado(request):
    if request.method == 'GET':
        categorias = Categoria.objects.all()
        serializer = CategoriaSerializar(categorias, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = CategoriaSerializar(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','POST'])
def marca_listado(request):
    if request.method == 'GET':
        marcas = Marca.objects.all()
        serializer = MarcaSerializar(marcas, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = MarcaSerializar(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def producto_detalle(request,pk):
    try:
        producto = Producto.objects.get(id=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = ProductoSerializar(producto)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = ProductoSerializar(producto,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        producto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET','PUT','DELETE'])
def categoria_detalle(request,pk):
    try:
        categoria = Categoria.objects.get(id=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = CategoriaSerializar(categoria)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = CategoriaSerializar(categoria,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        categoria.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET','PUT','DELETE'])
def marca_detalle(request,pk):
    try:
        marca = Marca.objects.get(id=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = MarcaSerializar(marca)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = MarcaSerializar(marca,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        marca.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
