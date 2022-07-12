from django.http import JsonResponse


#para trabajar con djangorestframework
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

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

#### ENDPOINTS PROFESOR
from .models import Profesor
from .serializers import ProfesorSerializer

@api_view(['GET','POST'])
def profesor(request):
    if request.method == 'GET':
        dataProfesor = Profesor.objects.all()
        serProfesor = ProfesorSerializer(dataProfesor,many=True)

        return Response(serProfesor.data)
    
    elif request.method == 'POST':
        serProfesor = ProfesorSerializer(data=request.data)
        if serProfesor.is_valid():
            serProfesor.save()
            return Response(serProfesor.data)
        else:
            return Response(serProfesor.errors,status=status.HTTP_400_BAD_REQUEST)

from django.core.exceptions import ObjectDoesNotExist

@api_view(['GET','PUT','DELETE'])
def profesor_detail(request,profesor_id):
    try:
        objProfesor = Profesor.objects.get(id=profesor_id)
    except ObjectDoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serProfesor = ProfesorSerializer(objProfesor)
        return Response(serProfesor.data)
    
    elif request.method =='PUT':
        serProfesor = ProfesorSerializer(objProfesor,data=request.data)
        if serProfesor.is_valid():
            serProfesor.save()
            return Response(serProfesor.data)
        else:
            return Response(serProfesor.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method =='DELETE':
        objProfesor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
