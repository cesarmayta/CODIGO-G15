from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics

from .models import *
from .serializers import *

class IndexView(APIView):

    def get(self,request):
        context = {
            'status':True,
            'message':'api de miembros listo'
        }

        return Response(context)

class CategoriaView(generics.ListAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class CursoView(generics.ListAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

class CursoDetailView(APIView):

    def get(self,request,curso_id):
        data = Curso.objects.get(pk=curso_id)
        serData = CursoSerializer(data)

        context = {
            'status':True,
            'content':serData.data
        }

        return Response(context)

class CategoriaCursoView(APIView):

    def get(self,request,categoria_id):
        data = Categoria.objects.get(pk=categoria_id)
        serData = CategoriaCursoSerializer(data)

        context = {
            'status':True,
            'content':serData.data
        }

        return Response(context)

class UserCreateView(generics.CreateAPIView):
    serializer_class = UserSerializer

class MiembroCreateView(generics.CreateAPIView):
    serializer_class = MiembroSerializer

from rest_framework_simplejwt.views import TokenObtainPairView


class LoginView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
