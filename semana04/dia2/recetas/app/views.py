from django.shortcuts import render


from .models import Receta

# Create your views here.
def index(request):
    listaRecetas = Receta.objects.all() #select * from app_receta
    print(listaRecetas)

    context = {
        'recetas':listaRecetas
    }
    return render(request,'index.html',context)

