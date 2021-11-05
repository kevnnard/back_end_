from rest_framework import serializers
from mujerApp.models.centro import Centro

class CentroSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Centro
        fields = ['nombre', 'direccion', 'email', 'telefono']

    def create(self, validated_data):
        centroInstance = Centro.objects.create(**validated_data)
        return centroInstance

    def to_representation(self, obj):
        centro = Centro.objects.get(idcentro=obj.idcentro)
        return {
            'idcentro': centro.idcentro,
            'nombre': centro.nombre,
            'direccion': centro.direccion,
            'email': centro.email,
            'telefono': centro.telefono
        }

