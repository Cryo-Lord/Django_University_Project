import datetime
from xmlrpc.client import DateTime
from django import forms
from Inventario.choices import disponibilidades
from Inventario.models import Categoria,Producto,Marca
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UsuarioForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name','email','password1','password2']

class ProductoForm(forms.ModelForm):
    nombre = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Ej: Tijeras"}))
    categoria = forms.ModelChoiceField(
        queryset=Categoria.objects.all(),
        empty_label="Selecciona su categoría",
        widget=forms.Select(attrs={"class":"form-control"})
    )
    marca = forms.ModelChoiceField(
        queryset=Marca.objects.all(),
        empty_label="Selecciona su marca",
        widget=forms.Select(attrs={"class":"form-control"})
    )
    precio = forms.CharField(widget=forms.NumberInput(attrs={"class":"form-control","placeholder":"ingrese su precio"}))
    disponibilidad = forms.CharField(widget=forms.Select(choices=disponibilidades, attrs={"class":"form-select"}))
    cantidad = forms.CharField(widget=forms.NumberInput(attrs={"class":"form-control","placeholder":"ingrese la cantidad añadida"}))

    def clean_precio(self):
        precio = self.cleaned_data['precio']
        try:
            precio = int(precio)
        except ValueError:
            raise forms.ValidationError('El precio debe ser un número entero')
        if precio <= 0:
            raise forms.ValidationError("El precio debe ser mayor que cero")
        return precio

    class Meta:
        model = Producto
        fields = '__all__'

class MarcaForm(forms.ModelForm):
    nombre = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Ej: Becker', 'class':'form-control'}))
    imagen = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Solo jpg, jpeg, webp'}),required=False)
    descripcion = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Descripción de la marca'}))

    class Meta:
        model = Marca
        fields = '__all__'

class CategoriaForm(forms.ModelForm):
    nombre = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Ej: Herramientas', 'class':'form-control'}))
    imagen = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Cargar imagen','class':'form-control'}),required=False)
    descripcion = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Descripción de la categoria'}))

    class Meta:
        model = Categoria
        fields = '__all__'