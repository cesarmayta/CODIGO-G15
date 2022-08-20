from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view()),
    path('categoria',views.CategoriaView.as_view()),
    path('curso',views.CursoView.as_view())
]
