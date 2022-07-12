from django.http import JsonResponse

#para trabajar con djangorestframework
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
from .models import Alumno

def index(request):
    context = {
        'mensaje':'Bienvenido a mi API con django'
    }
    return JsonResponse(context)

@api_view(['GET'])
def home(request):
    context = {
        'status':True,
        'content':'Bienvenido a mi API con DRF'
    }

    return Response(context)

def alumnos(request):
    dataAlumnos = Alumno.objects.all()
    #serializamos los resultados
    listAlumnos = []
    for alumno in dataAlumnos:
        dicAlumno = {
            'nombre':alumno.nombre,
            'email':alumno.email
        }
        listAlumnos.append(dicAlumno)

    context = {
        'status':True,
        'content':listAlumnos
    }
    return JsonResponse(context)

######### aplicando serializers de drf #########

from .serializers import AlumnoSerializer

@api_view(['GET'])
def getAlumnos(request):
    dataAlumnos = Alumno.objects.all()
    serAlumnos = AlumnoSerializer(dataAlumnos,many=True)

    context = {
        'status':True,
        'content':serAlumnos.data
    }

    return Response(context)

@api_view(['POST'])
def setAlumno(request):
    serAlumno = AlumnoSerializer(data=request.data)
    serAlumno.is_valid(raise_exception=True)

    nuevoAlumno = serAlumno.save()

    context = {
        'status':True,
        'content':AlumnoSerializer(nuevoAlumno).data
    }

    return Response(context)
