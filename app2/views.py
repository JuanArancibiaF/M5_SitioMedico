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
        print("El POST contiene:", request.POST)

        formulario_devuelto = FormularioBusqueda(request.POST)
        usuario_data = verificar_user(formulario_devuelto)

        if formulario_devuelto.is_valid() == True and usuario_data != False:
            context = {'usuario': usuario_data}
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
    print(type(lista_usuarios))
    print(lista_usuarios)
    for pacientes in lista_usuarios:
        print('holaaaaaaaaaaaaaaaaaaaa')
        print(pacientes)
        if pacientes.rut == run_usuario:
            return pacientes
        else:
            continue
    return False


def context_lista_pacientes():
    filename= "/app2/data/pacientes.json"
    with open(str(settings.BASE_DIR)+filename, 'r') as file:
        pacientes=json.load(file)
    context = {'lista_pacientes': pacientes['pacientes']}
    return context


def lista_pacientes(request):
    context = context_lista_pacientes()
    return render(request, 'app2/fichapaciente.html', context)

