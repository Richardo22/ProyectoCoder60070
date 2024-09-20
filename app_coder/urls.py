from django.urls import path
from app_coder.views import *

urlpatterns = [
    path('agrega-curso/<nombre>/<camada>', crea_curso),
    path('lista-cursos/', lista_curso),
    path ('',inicio),
    path ('estudiantes',estudiantes),
    path ('cursos', curso),
    path ('entregables',entregables),
    path ('profesores',profesores),
]
