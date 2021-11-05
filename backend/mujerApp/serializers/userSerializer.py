from rest_framework import serializers
from mujerApp.models.user import User
# from mujerApp.models.centro import Centro
from mujerApp.models.solicitud import Solicitud
from mujerApp.serializers.solicitudSerializer import SolicitudSerializer



class UserSerializer(serializers.ModelSerializer):
    #solicitud = SolicitudSerializer()
    class Meta:
        model = User
        fields = ['cedula', 'username', 'password', 'nombre', 'direccion', 'email', 'telefono']

    def create(self, validated_data):
        #solicitudData = validated_data.pop('solicitud')
        userInstance = User.objects.create(**validated_data)
        # Centro.objects.create(user=userInstance, **solicitudData)
        #Solicitud.objects.create(user=userInstance, **solicitudData)
        return userInstance

    def to_representation(self, obj):
        user = User.objects.get(cedula=obj.cedula)
        #solicitud = Solicitud.objects.get(iduser=obj.cedula)
        #centro = Centro.objects.get(solicitud=obj.id)
        return {
            'cedula': user.cedula,
            'username': user.username,
            'password': user.password,
            'nombre': user.nombre,
            'direccion':user.direccion,
            'email': user.email,
            'telefono': user.telefono
        }