from django.urls import path
from . import views

urlpatterns = [
    path('salvar_visitante/', views.salvar_visitante, name='salvar_visitante'),
    path('salvar_entrada/', views.salvar_entrada, name='salvar_entrada'),
    path('salvar_usuario/', views.salvar_usuario, name='salvar_usuario'),
    path('salvar_departamento/', views.salvar_departamento, name='salvar_departamento'),
]
