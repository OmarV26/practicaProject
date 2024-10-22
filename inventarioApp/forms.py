from django import forms


class ProductoForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    precio = forms.DecimalField(max_digits=10, decimal_places=2)
    stock = forms.IntegerField()

    nombre.widget.attrs['class'] = 'form-control'
    precio.widget.attrs['class'] = 'form-control'
    stock.widget.attrs['class'] = 'form-control'

class EmpleadoForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    apellido = forms.CharField(max_length=100)
    email = forms.CharField(max_length=100)
    telefono = forms.CharField(max_length=100)

    nombre.widget.attrs['class'] = 'form-control'
    apellido.widget.attrs['class'] = 'form-control'
    email.widget.attrs['class'] = 'form-control'
    telefono.widget.attrs['class'] = 'form-control'