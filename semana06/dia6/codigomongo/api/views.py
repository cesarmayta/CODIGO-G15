from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Alumno
from .serializers import AlumnoSerializer

class AlumnoView(APIView):

    def get(self,request):
        data = Alumno.objects.all()
        serData = AlumnoSerializer(data,many=True)
        return Response(serData.data)

    def post(self,request):
        serData = AlumnoSerializer(data=request.data)
        serData.is_valid(raise_exception=True)
        serData.save()

        return Response(serData.data)