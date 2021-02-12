from django.urls import path
from . import views


app_name='app2'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('registro/', views.registro, name='registro'),
    path('login/', views.login, name='login'),
    path('fichaPaciente/', views.lista_pacientes, name='fichaPaciente'),
    path('fichaMedica/', views.fichaMedica, name='fichaMedica'),
    path('calendario/', views.calendarioHoras, name='calendario'),
    path('administracion/', views.administracion, name='administracion'),
]