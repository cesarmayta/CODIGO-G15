from rest_framework.views import APIView
from rest_framework.response import Response

from .models import (
    Mesa,Categoria
)

from .serializers import(
    MesaSerializer,
    CategoriaSerializer
)

class IndexView(APIView):

    def get(self,request):
        context = {
            'ok':True,
            'content':'POS API activo'
        }

        return Response(context)

class MesaView(APIView):

    def get(self,request):
        data = Mesa.objects.all()
        serializerData = MesaSerializer(data,many=True)

        context = {
            'ok':True,
            'content':serializerData.data
        }

        return Response(context)

class CategoriaView(APIView):

    def get(self,request):
        data = Categoria.objects.all()
        serializerData = CategoriaSerializer(data,many=True)

        context = {
            'ok':True,
            'content':serializerData.data
        }

        return Response(context)