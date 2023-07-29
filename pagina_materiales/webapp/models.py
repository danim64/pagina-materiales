from django.db import models

# Create your models here.


class Grupo(models.Model):
    categoria = models.CharField(max_length=150)
    subcategoria = models.CharField(max_length=150,blank=True,null=True)
    
    def __str__(self):
        return f"{self.categoria}"
    class Meta:
        verbose_name_plural = "grupos"

class Marca(models.Model):
    nombre = models.CharField(max_length=150)
    
    def __str__(self):
        return f"{self.nombre}"
    
class Proveedor(models.Model):
    nombre = models.CharField(max_length=60)
    direccion = models.CharField(max_length=40,blank=True,null=True)
    ciudad = models.CharField(max_length=40,blank=True,null=True)
    telefono = models.CharField(max_length=15,blank=True,null=True)
    vendedor = models.CharField(max_length=40,blank=True,null=True)
    
    def __str__(self):
        return f"{self.nombre}"
    
    class Meta:
        verbose_name_plural = "proveedores"

class Unidad(models.Model):
    unidad = models.CharField(max_length=30)
    def __str__(self):
        return f"{self.unidad}"


class Materiales(models.Model):
    descripcion = models.CharField(max_length=150)
    precio = models.IntegerField()
    fecha_precio = models.DateTimeField(auto_now=True)
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    unidad = models.ForeignKey(Unidad, on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.descripcion}"
    
    class Meta:
        verbose_name_plural = "materiales" 


