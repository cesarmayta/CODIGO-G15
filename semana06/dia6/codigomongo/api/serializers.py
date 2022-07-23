from rest_framework_mongoengine.serializers import DocumentSerializer

from .models import Alumno

class AlumnoSerializer(DocumentSerializer):
    class Meta:
        model = Alumno
        fields = ('nombre','email','celular','github')
        extra_kwars = {'id':{'read_only':True}}