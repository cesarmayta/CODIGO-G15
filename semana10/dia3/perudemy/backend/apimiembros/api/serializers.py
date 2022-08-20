from dataclasses import fields
from turtle import clear


from rest_framework import serializers

from .models import *

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'

class MiembroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Miembro
        fields = '__all__'

class CategoriaCursoSerializer(serializers.ModelSerializer):
    Cursos = CursoSerializer(many=True,read_only=True)
    
    class Meta:
        model = Categoria
        fields = ['categoria_id','categoria_nombre','Cursos']