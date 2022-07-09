from django.shortcuts import render

from .models import Categoria,Marca,Producto

from .carrito import Cart

################### CATALOGO DE PRODUCTOS
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

def producto(request,producto_id):
    objProducto = Producto.objects.get(pk=producto_id)
    context = {
        'producto':objProducto
    }
    return render(request,'producto.html',context)

def productosPorCategoria(request,categoria_id):
    objCategoria = Categoria.objects.get(pk=categoria_id)
    listaProductos = objCategoria.producto_set.all()

    listaCategorias = Categoria.objects.all()
    listaMarcas = Marca.objects.all()
    context = {
        'marcas':listaMarcas,
        'categorias':listaCategorias,
        'productos':listaProductos
    }

    return render(request,'index.html',context)

def productosPorMarca(request,marca_id):
    objMarca = Marca.objects.get(pk=marca_id)
    listaProductos = objMarca.producto_set.all()

    listaCategorias = Categoria.objects.all()
    listaMarcas = Marca.objects.all()
    context = {
        'marcas':listaMarcas,
        'categorias':listaCategorias,
        'productos':listaProductos
    }

    return render(request,'index.html',context)

def productosPorNombre(request):
    nombre = request.POST['nombre']
    print('valor a buscar : ' + nombre)
    listaProductos = Producto.objects.filter(nombre__contains=nombre)

    listaCategorias = Categoria.objects.all()
    listaMarcas = Marca.objects.all()
    context = {
        'marcas':listaMarcas,
        'categorias':listaCategorias,
        'productos':listaProductos
    }

    return render(request,'index.html',context)


############################ CARRITO DE COMPRAS ############

def carrito(request):
    return render(request,'carrito.html')

def agregarCarrito(request,producto_id):
    if request.method == 'POST':
        cantidad = int(request.POST['cantidad'])
    else:
        cantidad  = 1
    objProducto = Producto.objects.get(pk=producto_id)
    carritoProducto = Cart(request)
    carritoProducto.add(objProducto,cantidad)
    print(request.session.get("cart"))

    return render(request,'carrito.html')


############################# CUENTA DE USUARIO
def login(request):
    return render(request,'login.html')