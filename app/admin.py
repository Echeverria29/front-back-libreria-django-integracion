from django.contrib import admin
from django import forms
from .models import *

class ClienteAdmin(admin.ModelAdmin):
    list_display = ['user','rut','nombre','apellido','correo', 'direccion','telefono']
    search_fields = ['id']
    list_per_page = 4

class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ['user','rut','nombre','apellido','correo', 'direccion','telefono','cargo','departamento']
    search_fields = ['id']
    list_per_page = 5

class tecnicoAdmin(admin.ModelAdmin):
    list_display = ['user','rut','nombre','apellido','correo', 'direccion','telefono']
    search_fields = ['id']
    list_per_page = 10

class LibroAdmin(admin.ModelAdmin):
    list_display = ['id','nombre','autor','editorial', 'precio','stock','proveedor']
    search_fields = ['id']
    list_per_page = 6

class carritoAdmin(admin.ModelAdmin):
    list_display = ['id','libro','cantidad']
    search_fields = ['id']
    list_per_page = 7

class materialesAdmin(admin.ModelAdmin):
    list_display = ['id','nombre','stock','tecnico_id']
    search_fields = ['id']
    list_per_page = 8

class tipoAdmin(admin.ModelAdmin):
    list_display = ['id','tipo']
    search_fields = ['id']
    list_per_page = 9


class servicioAdmin(admin.ModelAdmin):
    list_display = ['id','fecha_servicio','direccion_servicio','detalle_servicio','tecnico','cliente']
    search_fields = ['id']
    list_per_page = 11

class ventaAdmin(admin.ModelAdmin):
    list_display = ['id','fecha_venta','cliente_id','empleado_id']
    search_fields = ['id']
    list_per_page = 12


class pagoAdmin(admin.ModelAdmin):
    list_display = ['id','total','venta_id']
    search_fields = ['id']
    list_per_page = 13

class cotizacionesAdmin(admin.ModelAdmin):
    list_display = ['id','fecha','correo','detalle','cliente_id']
    search_fields = ['id']
    list_per_page = 14






admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Empleado, EmpleadoAdmin)
admin.site.register(Tecnico, tecnicoAdmin)
admin.site.register(Servicio, servicioAdmin)
admin.site.register(Libro, LibroAdmin)
admin.site.register(Pago, pagoAdmin)
admin.site.register(Venta, ventaAdmin)
admin.site.register(Carrito, carritoAdmin)
admin.site.register(Materiales, materialesAdmin)
admin.site.register(Tipo, tipoAdmin)
admin.site.register(Cotizaciones,cotizacionesAdmin)