from django.db import models
from datetime import datetime

class Categoria(models.Model):
    nombre = models.CharField(max_length=150, verbose_name='Nombre de la categoria')
    descripcion = models.CharField(max_length=500, verbose_name='Descripcion de la categoria')
    fechaRegistro = models.DateField(default=datetime.now, verbose_name='Fecha de registro')

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Nombre de la categoria'
        verbose_name_plural = 'Categorias'

        ordering = ['id']


class Producto(models.Model):
    nombre = models.CharField(max_length=150, verbose_name='Nombre del Producto')
    stock = models.PositiveIntegerField(default=0)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, verbose_name='Categoria')
    precio = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    imagen = models.ImageField(upload_to='imagen/%Y/%m/%d', null=True, blank=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

        ordering = ['id']