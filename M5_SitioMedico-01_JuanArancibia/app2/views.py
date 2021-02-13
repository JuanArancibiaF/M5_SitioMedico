import json
import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings
from .forms import FormularioBusqueda

# Create your views here.

def inicio(request):
    return render(request, 'app2/index.html')

def registro(request):
    return render(request, 'app2/register.html')

def login(request):
    return render(request, 'app2/login.html')

def calendarioHoras(request):
    return render(request, 'app2/calendarioHoras.html')

def administracion(request):
    return render(request, 'app2/administracion.html')


def fichaMedica(request):
    formulario = FormularioBusqueda()
    if request.method == "GET":
        formulario = FormularioBusqueda()
        context = {'formulario': formulario, 'invalid': False}
        print(context)
        return render(request, 'app2/fichamedica.html', context)

    elif request.method == "POST":
        #print("El POST contiene:", request.POST)
        formulario_devuelto = FormularioBusqueda(request.POST)
        usuario_data = False
        print(formulario_devuelto)
        if formulario_devuelto.is_valid() == True:
            formulario_rut = formulario_devuelto.cleaned_data
            print(formulario_rut, '########################################')
            usuario_data = verificar_user(formulario_rut)

        if usuario_data != False:
            lista_examenes = contex_examenes_paciente()
            context = {'usuario': usuario_data, 'lista_examenes': lista_examenes['lista_examenes']}
            return render(request, 'app2/fichapaciente.html', context)
        elif formulario_devuelto.is_valid() == False:
            formulario = FormularioBusqueda()
            context = {'formulario': formulario, 'invalid': True}
            return render(request, 'app2/fichamedica.html', context)
        else:
            formulario = FormularioBusqueda()
            context = {'formulario': formulario, 'invalid': True}
            return render(request, 'app2/fichamedica.html', context)
    else:
        formulario = FormularioBusqueda()
        context = {'formulario': formulario, 'invalid': True}
        return render(request, 'app2/fichamedica.html', context)


def verificar_user(run_usuario):
    lista_usuarios = context_lista_pacientes()
    for paciente in lista_usuarios['lista_pacientes']:
        print(paciente.get('rut'))
        print(run_usuario.get('Rut'))
        if paciente.get('rut') == run_usuario.get('Rut'):
            
            return paciente
        else:
            continue
    return False


def context_lista_pacientes():
    filename = "/app_forms/data/pacientes.json"
    with open(str(settings.BASE_DIR)+filename, 'r') as file:
        pacientes = json.load(file)
    context = {'lista_pacientes': pacientes['pacientes']}
    return context


def lista_pacientes(request):
    context = context_lista_pacientes()
    return render(request, 'app2/fichapaciente.html', context)


def contex_examenes_paciente():
    filename = "/app2/data/examenes.json"
    with open(str(settings.BASE_DIR)+filename, 'r') as file:
        examenes = json.load(file)
    context = {'lista_examenes' : examenes['examenes']}
    return context

