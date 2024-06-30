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