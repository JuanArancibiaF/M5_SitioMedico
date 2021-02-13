from django.shortcuts import render
from django.template import loader, context
from django.http import HttpResponse
from django.http import HttpResponsePermanentRedirect


# Create your views here.

def inicio(request):
    return render(request, 'app1/index.html')

def registro(request):
    return render(request, 'app1/register.html')



def login(request):
    return render(request, 'app1/login.html')

def fichaPaciente(request):
    return render(request, 'app1/fichapaciente.html')


def calendarioHoras(request):
    return render(request, 'app1/calendarioHoras.html')

def administracion(request):
    return render(request, 'app1/administracion.html')