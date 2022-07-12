from django.http import JsonResponse

# Create your views here.

def index(request):
    context = {
        'mensaje':'Bienvenido a mi API con django'
    }
    return JsonResponse(context)