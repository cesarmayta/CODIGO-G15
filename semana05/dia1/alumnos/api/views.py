from multiprocessing.dummy import JoinableQueue
from django.http import JsonResponse

# Create your views here.
from .models import Alumno

def index(request):
    context = {
        'mensaje':'Bienvenido a mi API con django'
    }
    return JsonResponse(context)

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