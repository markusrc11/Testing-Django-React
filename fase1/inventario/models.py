from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    SKU = models.CharField(unique=True, max_length=50, validators=[RegexValidator(regex='^ING-\d{4}$', message='SKU debe tener el formato ING-XXXX donde XXXX son dígitos.')])
    cantidad = models.PositiveIntegerField()
    ultima_actualizacion = models.DateTimeField(auto_now=True)
