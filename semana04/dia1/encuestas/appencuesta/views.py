from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def mostrar_encuesta(request):
    return HttpResponse('<h1>Encuesta Nro 1</h1>')

def pregunta(request,pregunta_id):
    return HttpResponse('pregunta nro %s' % pregunta_id)