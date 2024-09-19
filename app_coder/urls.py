from django.urls import path
from app_coder.views import crea_curso, lista_curso, profesores

urlpatterns = [
    path('agrega-curso/<nombre>/<camada>', crea_curso),
    path('lista-cursos/', lista_curso),
    path ('profesores',profesores),
]
