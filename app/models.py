from django import forms
from django.db import models

class Cliente(models.Model):
    id = models.IntegerField(primary_key=True)
    rut_cliente = models.CharField( max_length=15)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    correo = models.CharField(max_length=80)
    direccion = models.CharField(max_length=80)
    telefono = models.CharField(max_length=20)
    numero_tarjeta = models.IntegerField()


    def __str__(self):
      return self.rut_cliente


    class Meta:
       
        db_table = 'cliente'

class Cotizaciones(models.Model):
    id = models.IntegerField(primary_key=True)
    fecha = models.DateTimeField()
    correo = models.CharField(max_length=80)
    detalle = models.CharField(max_length=200)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def __str__(self):
      return self.cliente


    class Meta:
       
        db_table = 'cotizaciones'



class Tecnico(models.Model):
    id = models.IntegerField(primary_key=True)
    rut_tecnico = models.CharField( max_length=15)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    correo = models.CharField(max_length=80)
    direccion = models.CharField(max_length=80)
    telefono = models.CharField(max_length=20)
    
    def __str__(self):
        return self.rut_tecnico
    
    class Meta:
        
        db_table = 'tecnico'


class Materiales(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField( max_length=30)
    stock = models.IntegerField()
    tecnico = models.ForeignKey(Tecnico, models.CASCADE)

    class Meta:
        
        db_table = 'materiales'




class Empleado(models.Model):
    id = models.IntegerField(primary_key=True)
    rut_empleado = models.CharField( max_length=15)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    correo = models.CharField(max_length=80)
    direccion = models.CharField(max_length=80)
    telefono = models.CharField(max_length=20)
    cargo = models.CharField(max_length=50)
    departamento = models.CharField(max_length=50)

    def __str__(self):
        return self.rut_empleado
  
    class Meta:
        
        db_table = 'empleado'

class Tipo(models.Model):
    id = models.IntegerField(primary_key=True)
    tipo = models.CharField(max_length=40)

    def __str__(self):
        return self.tipo
    class Meta:
        
        db_table = 'tipo'

class Servicio(models.Model):
    id = models.IntegerField(primary_key=True)
    fecha_servicio = models.DateTimeField()
    direccion_servicio = models.CharField(max_length=80)
    detalle_servicio = models.CharField(max_length=200)
    tipo = models.ForeignKey(Tipo,on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    tecnico = models.ForeignKey(Tecnico, on_delete=models.CASCADE)
    
    
    
    class Meta:
        db_table = 'servicio'


class Venta(models.Model):
    id = models.IntegerField(primary_key=True)
    fecha_venta = models.DateField()
    total = models.IntegerField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)

    class Meta:
        
        db_table = 'venta'

class Pago(models.Model):
    id = models.IntegerField(primary_key=True)
    total = models.IntegerField()
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    def __str__(self):
        return self.total
    class Meta:
       
        db_table = 'pago'


class Libro(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    autor = models.CharField(max_length=50)
    editorial = models.CharField(max_length=50)
    precio = models.IntegerField()
    stock = models.IntegerField()
    proveedor = models.CharField(max_length=50)

    def stockfinal(self):
      return self.stock - self.carrito.cantidad

    def __str__(self):
      return self.nombre
  

    class Meta:
       
        db_table = 'libro'

class Carrito(models.Model):
    id = models.IntegerField(primary_key=True)
    libro = models.ForeignKey(Libro, models.CASCADE)
    cantidad = models.PositiveIntegerField()
    
    def subtotal(self):
        return self.libro.precio * self.cantidad

    def __str__(self):
        return self.libro.nombre
    
    class Meta:
        
        db_table = 'carrito'

class DetalleVenta(models.Model):
    id = models.IntegerField(primary_key=True)
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE)  
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)

    class Meta:
        
        db_table = 'detalle_venta'
      



