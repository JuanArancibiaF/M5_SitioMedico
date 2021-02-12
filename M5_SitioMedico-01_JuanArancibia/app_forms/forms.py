from django import forms
from django.core import validators


class FormularioPacientes(forms.Form):
    rut = forms.CharField()
    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.CharField()
    tutor = forms.CharField()
    direccion = forms.CharField()
    enfermedades = forms.CharField()



