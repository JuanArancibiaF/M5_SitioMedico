import json


from django.shortcuts import render, redirect
from .forms import FormularioPacientes, tipos_examenes

from django.conf import settings


def crear_pacientes(request):
        if request.method=="GET":
            formulario = FormularioPacientes()
            contex = {'formulario':formulario}
            return render(request, 'app_forms/crear_pacientes.html', contex)

        elif request.method=="POST":
            print ("llego POST OK", request.POST)
            
            formulario_devuelto = FormularioPacientes(request.POST)
            
        if formulario_devuelto.is_valid() == True:
            datos_formulario = formulario_devuelto.cleaned_data
            filename = "/app_forms/data/pacientes.json"
            with open (str(settings.BASE_DIR)+filename, 'r') as file:  
                pacientes=json.load(file)
                pacientes['pacientes'].append(datos_formulario)
            with open (str(settings.BASE_DIR)+filename, 'w') as file:
                json.dump(pacientes, file)
            return redirect('app_forms:pacientes_creados')
        else:
            contex = {'formulario':formulario_devuelto}
            return render (request, 'app_forms/crear_pacientes.html', contex )



def lista_pacientes(request):
    filename = "/app_forms/data/pacientes.json"
    with open (str(settings.BASE_DIR)+filename, 'r') as file:
                pacientes=json.load(file)
    contex = {'lista_pacientes': pacientes['pacientes']} 
    return render(request, 'app_forms/lista_pacientes.html', contex)   

def eliminar_pacientes(request, rut):

    if request.method == "GET":
        context = {'rut': rut}
        return render(request, "app_forms/eliminar_pacientes.html", context)

    if request.method == "POST":
        filename= "/app_forms/data/pacientes.json"
        with open(str(settings.BASE_DIR)+filename, 'r') as file:
            data=json.load(file)
        for paciente in data['pacientes']:
            if str(paciente['rut'])==str(rut):
                data['pacientes'].remove(paciente)
                break
        with open(str(settings.BASE_DIR)+filename, 'w') as file:
            json.dump(data, file)
        
        return redirect('app_forms:pacientes_creados')

def pacientes_creados(request):
    filename = "/app_forms/data/pacientes.json"
    with open (str(settings.BASE_DIR)+filename, 'r') as file:
                pacientes=json.load(file)
    contex = {'lista_pacientes': pacientes['pacientes']}
    return render(request, 'app_forms/pacientes_creados.html',contex)

def ingresar_examenes(request):
    if request.method == "GET":
        examenes = tipos_examenes()
        context = {'examenes': examenes}
        return render(request, 'app_forms/ingresar_examenes.html', context)

    elif(request.method == "POST"):
        #print("EL POST CONTIENE: ", request.POST)
        examenes_post = tipos_examenes(request.POST) 
        print(type(examenes_post))
        if examenes_post.is_valid() == True:
            data = examenes_post.cleaned_data
            print(data)
            data['fecha']=data['fecha'].strftime("%Y-%m-%d")
            print("EL POST CONTIENE: ", data)
            archivo = "/app2/data/examenes.json" 
            with open(str(settings.BASE_DIR)+archivo,'r') as file:
                examenes = json.load(file)
                examenes['examenes'].append(data)
            with open(str(settings.BASE_DIR)+archivo,'w') as file:
                json.dump(examenes, file)
            return redirect('app2:fichaMedica')
        else:
            context = {'examenes': examenes_post}
            return render(request, 'app_forms/ingresar_examenes.html', context)         
