from django.urls import path
from app_coder.views import *

urlpatterns = [
    path('agrega-curso/<nombre>/<camada>', crea_curso),
    path('lista-cursos/', lista_curso),
    path ('',inicio),
    path ('estudiantes/',estudiantes, name='estudiantes'),
    path ('curso/', cursos, name='cursos'),
    path ('entregables/',entregables, name='entregables'),
    path ('profesores/',profesores, name='profesores'),
    path ('curso-formulario/',curso_formulario, name='CursoFormulario'),
]
