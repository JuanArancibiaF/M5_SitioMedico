from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def inicio(request):
    return render(request, 'app2/index.html')

def registro(request):
    return render(request, 'app2/register.html')

def login(request):
    return render(request, 'app2/login.html')

def fichaPaciente(request):
    return render(request, 'app2/fichapaciente.html')

def fichaMedica(request):
    return render(request, 'app2/fichamedica.html')

def calendarioHoras(request):
    return render(request, 'app2/calendarioHoras.html')

def administracion(request):
    return render(request, 'app2/administracion.html')