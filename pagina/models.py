# models.py
from django.db import models
class Categoria(models.Model):
    id_categoria  = models.AutoField(db_column='idCategoria', primary_key=True) 
    categoria     = models.CharField(max_length=20, blank=False, null=False)

    def __str__(self):
        return str(self.categoria)

class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    nombre_producto = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    id_categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    foto = models.ImageField(upload_to='productos')
    activo = models.BooleanField(default=True)

    def __str__(self):
        return str(self.nombre_producto)
    class Meta:      
        ordering = ['id_producto']


class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    usuario = models.CharField(max_length=15)
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    apMaterno = models.CharField(max_length=20)
    correo = models.EmailField()
    rut = models.CharField(max_length=15)
    contraseña = models.CharField(max_length=20)
    confirmar_contraseña = models.CharField(max_length=20)
    edad = models.IntegerField()
    activo = models.BooleanField(default=True)

    def __str__(self):
        return str(self.usuario)
    class Meta:
        ordering = ['id_usuario']