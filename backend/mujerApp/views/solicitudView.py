from rest_framework import serializers, status, views
from rest_framework.response import Response
from mujerApp.models.solicitud import Solicitud

from mujerApp.serializers.solicitudSerializer import SolicitudSerializer

class SolicitudCreateView(views.APIView):
    def post(self, request, format=None):
        serializer = SolicitudSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SolicitudDeleteView(views.APIView):
    def delete(self, request, pk, format=None):
        solicitud = Solicitud.objects.get(id=pk)
        solicitud.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class SolicitudGetAllView(views.APIView):
    def get(request, format=None):
        solicitud= Solicitud.objects.all()
        serializer = SolicitudSerializer(solicitud, many=True)
        return Response(serializer.data)

class SolicitudGetView(views.APIView):
    def get(self, request, pk, format=None):
        solicitud = Solicitud.objects.get(id=pk)
        serializer = SolicitudSerializer(solicitud)
        return Response(serializer.data)

class SolicitudPutView(views.APIView):
    def put(self, request, pk, format=None):
        solicitud = Solicitud.objects.get(id=pk)
        serializer = SolicitudSerializer(solicitud, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)