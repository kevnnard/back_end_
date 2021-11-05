from django.db import models

class Centro(models.Model):
    idcentro = models.AutoField(primary_key=True, null=False)
    nombre = models.CharField('Nombre', max_length = 70, null=False)
    direccion = models.CharField('Direccion', max_length = 30, null=False)
    email = models.EmailField('Email', max_length = 100, null=False)
    telefono = models.IntegerField(null=False)
