from django.db import models
from .user import User
from .centro import Centro

class Solicitud(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    #iduser = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)
    cedula = models.BigIntegerField(null=False)
    idcentro = models.ForeignKey(Centro, related_name='centro', on_delete=models.CASCADE)
    nombreCliente = models.CharField('nombre', max_length = 30)
    ciudad = models.CharField('ciudad', max_length = 30, null=False)
    FinalizedState = models.BooleanField(default=False, null=False)
    mensaje = models.CharField(max_length= 1000, null= False)
    