from django.shortcuts import render

# Create your views here.

def inicio(request):
    return render(request, 'app1/index.html')

def registro(request):
    return render(request, 'app1/register.html')

def login(request):
    return render(request, 'app1/login.html')

def fichaPaciente(request):
    return render(request, 'app1/fichapaciente.html')

def fichaMedica(request):
    return render(request, 'app1/fichamedica.html')

def calendarioHoras(request):
    return render(request, 'app1/calendarioHoras.html')

def administracion(request):
    return render(request, 'app1/administracion.html')