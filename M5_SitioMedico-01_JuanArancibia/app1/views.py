from django.shortcuts import render, redirect
from django.template import loader, context
from django.http import HttpResponse
from django.http import HttpResponsePermanentRedirect
from .forms import FormularioBusqueda


# Create your views here.

def inicio(request):
    return render(request, 'app1/index.html')

def registro(request):
    return render(request, 'app1/register.html')


def fichaPaciente(request):
    return render(request, 'app1/fichapaciente.html')


def calendarioHoras(request):
    return render(request, 'app1/calendarioHoras.html')

def administracion(request):
    return render(request, 'app1/administracion.html')

def login(request):
    formulario = FormularioBusqueda()
    if request.method == "GET":
        formulario = FormularioBusqueda()
        context = {'formulario': formulario, 'invalid': False}
        return render(request, 'app1/login.html', context)

    elif request.method == "POST":
        formulario_devuelto = FormularioBusqueda(request.POST)

        if formulario_devuelto.is_valid() == True:
            data = formulario_devuelto.cleaned_data
            
            if data['Rut'] == '19220125-k' and data['contra'] == '12345':
                return redirect('app2:fichaMedica')
            else:
                return render(request, 'app1/login.html', context)

        
    return render(request, 'app1/login.html')