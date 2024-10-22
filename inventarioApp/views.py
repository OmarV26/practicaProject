from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from inventarioApp.models import *
from inventarioApp.forms import ProductoForm, EmpleadoForm

# Create your views here.

def Index(request):
    return render(request, 'inventarioApp/index.html')

def Productos(request):
    productos = Producto.objects.all()
    data = {'productos': productos}
    return render(request, 'inventarioApp/productos.html', data)

def Empleados(request):
    empleados = Empleado.objects.all()
    data = {'empleados': empleados}
    return render(request, 'inventarioApp/empleados.html',data)

def registroEmp(request):
    form = EmpleadoForm()

    if request.method == 'POST': # si el metodo es POST
        form = EmpleadoForm(request.POST) # crear un formulario con los datos que recibo
        if form.is_valid(): # validar el formulario
            Empleado.objects.create(nombre=form.cleaned_data['nombre'], apellido=form.cleaned_data['apellido'], email=form.cleaned_data['email'], telefono=form.cleaned_data['telefono']) # crear un objeto de empleado 
            return HttpResponseRedirect(reverse('empleados')) # redireccionar al objeto de empleado
    data = {'form': form} # agregar el formulario al diccionario
    return render(request, 'inventarioApp/registroEmp.html', data) # renderizar el formulario


def registroProd(request):
    form = ProductoForm()

    if request.method == 'POST':
        form = ProductoForm(request.POST) # para crear un formulario con los datos que recibo
        if form.is_valid(): #validar el formulario
            Producto.objects.create(nombre=form.cleaned_data['nombre'], precio=form.cleaned_data['precio'], stock=form.cleaned_data['stock']) # para crear un objeto de producto 
            return HttpResponseRedirect(reverse('productos')) # para redireccionar al objeto de producto
    data = {'form': form}
    return render(request, 'inventarioApp/registroProd.html', data)
