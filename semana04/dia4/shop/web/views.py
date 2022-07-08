from django.shortcuts import render

from .models import Categoria,Marca,Producto

# Create your views here.
def index(request):
    listaCategorias = Categoria.objects.all()
    listaMarcas = Marca.objects.all()
    listaProductos = Producto.objects.all()
    context = {
        'marcas':listaMarcas,
        'categorias':listaCategorias,
        'productos':listaProductos
    }
    return render(request,'index.html',context)

def producto(request):
    return render(request,'producto.html')

def carrito(request):
    return render(request,'carrito.html')

def login(request):
    return render(request,'login.html')