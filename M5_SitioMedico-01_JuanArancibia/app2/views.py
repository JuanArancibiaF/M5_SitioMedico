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



def calendarioHoras(request):
    return render(request, 'app2/calendarioHoras.html')

def administracion(request):
    return render(request, 'app2/administracion.html')


def fichaMedica(request):
    formulario = FormularioBusqueda()
    if request.method == "GET":
        formulario = FormularioBusqueda()
        context = {'formulario': formulario, 'invalid': False}
        return render(request, 'app2/fichamedica.html', context)

    elif request.method == "POST":
        formulario_devuelto = FormularioBusqueda(request.POST)
        usuario_data = False
        lista2=[]
        datos=[]

        #print(formulario_devuelto)
        if formulario_devuelto.is_valid() == True:
            formulario_rut = formulario_devuelto.cleaned_data
            #print(formulario_rut, '########################################')
            usuario_data = verificar_user(formulario_rut)

        if usuario_data != False:
            lista_examenes = contex_examenes_paciente()
            lista_examenes2 = []
            for i in range (0,len(lista_examenes['lista_examenes'])):
                lista2.append(lista_examenes['lista_examenes'][i]['rut'])

            #creamos una nueva lista de examenes solo con el rut solicitado
            rut = str(usuario_data['rut'])
            for i in range (0, len(lista2)):
                lista_examenes2.append(lista2[i].get(rut))
            print(len(lista_examenes2))
            #sacamos los elementos none ligados a otros rut
            for elemento in lista_examenes2:
                if elemento == None:
                    print("elemento none")
                else:
                    datos.append(elemento)
            examen_filtrado = {'colesterol':[],'triglicerido':[],'orina': [],'glucosa':[],'bilirrubina':[], 'fecha':[]}
            for elemento in datos:   
                examen_filtrado['colesterol'].append(elemento['colesterol'])
                examen_filtrado['triglicerido'].append(elemento['triglicerido'])
                examen_filtrado['orina'].append(elemento['orina'])
                examen_filtrado['glucosa'].append(elemento['glucosa'])
                examen_filtrado['bilirrubina'].append(elemento['bilirrubina'])
                examen_filtrado['fecha'].append(elemento['fecha'])
            print(examen_filtrado['fecha'])
            context = {'usuario': usuario_data, 'lista_examenes': lista_examenes2, 'resultados':examen_filtrado}
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

