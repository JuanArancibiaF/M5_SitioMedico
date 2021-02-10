import json
from django.shortcuts import render
from .forms import tipos_examenes
from django.conf import settings

# Create your views here.
def ingresar_examenes(request):
    if request.method == "GET":
        examenes = tipos_examenes()
        context = {'examenes': examenes}
        return render(request, 'formularios/ingresar_examenes.html', context)

    elif(request.method == "POST"):
        #print("EL POST CONTIENE: ", request.POST)
        examenes_post = tipos_examenes(request.POST) 
        if examenes_post.is_valid() == True:
            data = examenes_post.cleaned_data
            data['fecha']=data['fecha'].strftime("%Y-%m-%d")
            print("EL POST CONTIENE: ", data)
            archivo = "/formularios/data/examenes.json" 
            with open(str(settings.BASE_DIR)+archivo,'r') as file:
                examenes = json.load(file)
                examenes['examenes'].append(data)
            with open(str(settings.BASE_DIR)+archivo,'w') as file:
                json.dump(examenes, file)
            
            return render(request, 'formularios/ingreso_examenes_ok.html', context)
        else:
            context = {'examenes': examenes_post}
            return render(request, 'formularios/ingresar_examenes.html', context)

def ingreso_examenes_ok(request):
    with open(str(settings.BASE_DIR)+archivo,'r') as file:
        examenes = json.load(file)
        examenes['examenes'].append(data)
    context = {'lista_examenes': examenes['examenes'] }
    return render(request, '/formularios/ingreso_examenes_ok.html', context)