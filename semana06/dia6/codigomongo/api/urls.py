from django.urls import path

from . import views

urlpatterns = [
    path('alumno', views.AlumnoView.as_view()),
]
