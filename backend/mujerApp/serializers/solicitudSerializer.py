from mujerApp.models.centro import Centro
from mujerApp.models.solicitud import Solicitud
from rest_framework import serializers
from mujerApp.models.user import User
from mujerApp.serializers.centroSerializer import CentroSerializer

class SolicitudSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solicitud
        fields = ['nombreCliente', 'cedula', 'ciudad', 'FinalizedState', 'mensaje', 'idcentro']

    def create(self, validated_data):
        solicitudInstance = Solicitud.objects.create(**validated_data)
        return solicitudInstance

    def to_representation(self, obj):
        solicitud = Solicitud.objects.get(id=obj.id)
        return {
            'idSolicitud': solicitud.id,
            "cedula": solicitud.cedula,
            'nombreCliente': solicitud.nombreCliente,
            'ciudad': solicitud.ciudad,
            'FinalizedState': solicitud.FinalizedState,
            'Mensaje': solicitud.mensaje,
            'Centro': {
                "idCentro": solicitud.idcentro.idcentro,
                "direccion": solicitud.idcentro.direccion,
                "email": solicitud.idcentro.email,
                "telefono": solicitud.idcentro.telefono,
            }
        }






