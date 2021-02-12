from django.urls import path
from . import views


app_name='app_forms'

urlpatterns = [
    path('crear_pacientes/', views.crear_pacientes, name='crear_pacientes'),
    path('lista_pacientes/', views.lista_pacientes, name='lista_pacientes'),
    path('<rut>/eliminar_pacientes', views.eliminar_pacientes, name='eliminar_pacientes'),
    path('pacientes_creados/', views.pacientes_creados, name='pacientes_creados'),
]

 