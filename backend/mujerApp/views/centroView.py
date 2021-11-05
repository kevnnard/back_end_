from rest_framework import status, views
from rest_framework.response import Response

from mujerApp.serializers.centroSerializer import CentroSerializer
from mujerApp.models.centro import Centro

class CentroCreateView(views.APIView):
    def post(self, request, format=None):
        serializer = CentroSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CentroDeleteView(views.APIView):
    def delete(self, request, pk, format=None):
        centro = Centro.objects.get(idcentro=pk)
        centro.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CentroGetAllView(views.APIView):
    def get(request, format=None):
        centro = Centro.objects.all()
        serializer = CentroSerializer(centro, many=True)
        return Response(serializer.data)

class CentroGetView(views.APIView):
    def get(self, request, pk, format=None):
        centro = Centro.objects.get(idcentro=pk)
        serializer = CentroSerializer(centro)
        return Response(serializer.data)

class CentroPutView(views.APIView):
    def put(self, request, pk, format=None):
        centro = Centro.objects.get(idcentro=pk)
        serializer = CentroSerializer(centro, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)