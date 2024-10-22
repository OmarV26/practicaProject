from django.contrib import admin
from inventarioApp.models import *
# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'stock')

class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'email', 'telefono')

admin.site.register(Producto, ProductoAdmin)
admin.site.register(Empleado, EmpleadoAdmin)