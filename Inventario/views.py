from django.shortcuts import render,redirect, get_object_or_404
from Inventario import models as data
from django.template import loader
from django.http import HttpResponse, JsonResponse
from Inventario.forms import ProductoForm, MarcaForm, CategoriaForm, UsuarioForm
from django.contrib.auth import authenticate, login


# Create your views here.
def entrance(request):
    return render(request, 'entrance.html')

def Tome(request):
    return render(request, 'tome.html')

def Home(request):
    categorias = data.Categoria.objects.all()
    dato= {
        "categorias" : categorias
    }
    return render(request, "home.html", dato)

# Sector Usuarios --------------------------------------------------------------------->

def añadir_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
            login(request, user)
            return redirect('Select')
    else:
        form = UsuarioForm()

    return render(request, 'registration/register.html', {'form':form})  

# Sector Categorias ------------------------------------------------------------------->

def ver_categorias(request):
        
        categorias = data.Categoria.objects.all()
        dato = {
            "categorias" : categorias   
        }        
        return render(request, 'categoriaRead.html', dato )

def añadir_categoria(request):
    if request.method == "POST":
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Home')
    else:
        form = CategoriaForm()
    
    return render(request, 'categoriaAdd.html', {'form':form})

def cargar_editar_categoria(request, categoria_id):
    categoria = get_object_or_404(data.Categoria, id=categoria_id)
    form = CategoriaForm(instance=categoria)

    return render(request, 'categoriaEdit.html',{'form':form,'categoria':categoria})

def editar_categoria(request, categoria_id):
    categoria = get_object_or_404(data.Categoria, id=categoria_id)

    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect('/verCategorias/')
         
    else:
        form = CategoriaForm(instance=categoria)
    
    return render(request, 'buscador.html', {'form':form })

def eliminar_categoria(request, categoria_id):
    categoria = get_object_or_404(data.Categoria, id=categoria_id)
    if request.method == "POST":
        categoria.delete()
        return redirect('/verCategorias/')
    return render(request, 'categoriaDel.html')

# Sector Marcas ----------------------------------------------------------------------->

def ver_marcas(request):
        
        marcas = data.Marca.objects.all()
        dato = {
            "marcas" : marcas   
        }
        return render(request, 'marcaRead.html', dato )

def añadir_marca(request):
    if request.method == "POST":
        form = MarcaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Home')
    else:
        form = MarcaForm()
    
    return render(request, 'marcaAdd.html', {'form':form})

def cargar_editar_marca(request, producto_id):
    marca = get_object_or_404(data.Marca, id=producto_id)
    form = MarcaForm(instance=marca)

    return render(request, 'marcaEdit.html',{'form':form,'marca':marca})

def editar_marca(request, producto_id):
    marca = get_object_or_404(data.Marca, id=producto_id)

    if request.method == 'POST':
        form = MarcaForm(request.POST, instance=marca)
        if form.is_valid():
            form.save()
            return redirect('/verMarcas/')
         
    else:
        form = MarcaForm(instance=marca)
    
    return render(request, 'buscador.html', {'form':form})

def eliminar_marca(request, producto_id):
    producto = get_object_or_404(data.Producto, id=producto_id)
    if request.method == "POST":
        producto.delete()
        return redirect('/Categorias/{}'.format(request.POST['categoria']))
    return render(request, 'marcaDel.html')

# Sector Productos ---------------------------------------------------------------------->

def ver_productos(request, nombre_set):
        
        productos = data.Producto.objects.filter(categoria = nombre_set)
        dato = {
            "productos" : productos   
        }
        
        return render(request, 'productoRead.html', dato )

def añadir_producto(request):
    if request.method == "POST":
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/Categorias/{}'.format(request.POST['categoria']))
    else:
        form = ProductoForm()
    
    return render(request, 'productoAdd.html', {'form':form})

def cargar_editar_producto(request, producto_id):
    producto = get_object_or_404(data.Producto, id=producto_id)
    form = ProductoForm(instance=producto)

    return render(request, 'productoEdit.html',{'form':form,'producto':producto})

def editar_producto(request, producto_id):
    producto = get_object_or_404(data.Producto, id=producto_id)
    categoria = get_object_or_404(data.Categoria, nombre=producto.categoria) #Solo las foreign key pueden llamarse así
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('/Categorias/{}'.format(categoria.__dict__['id']))
         
    else:
        form = ProductoForm(instance=producto)
    
    return render(request, '/Categorias/{}'.format(categoria.__dict__['id']), {'form':form})

def eliminar_producto(request, producto_id):
    producto = get_object_or_404(data.Producto, id=producto_id)
    categoria = get_object_or_404(data.Categoria, nombre=producto.categoria) #Solo las foreign key pueden llamarse así
    if request.method == "POST":
        producto.delete()
        return redirect('/Categorias/{}'.format(categoria.__dict__['id']))
    return render(request, 'productoDel.html', {'producto':producto, 'categoria':categoria})