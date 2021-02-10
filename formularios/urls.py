from django.urls import path
from . import views


app_name='formularios'

urlpatterns = [
    path('ingresar_examenes', views.ingresar_examenes, name='ingresar_examenes'),
    path('ingreso_examenes_ok', views.ingreso_examenes_ok, name='ingreso_examenes_ok'),
]