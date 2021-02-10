from django import forms
from django.core import validators
#Problemas integrando Validators

class tipos_examenes(forms.Form):

    orina = forms.CharField(validators = [validators.MinLengthValidator(3,"noooo")])
    glucosa = forms.IntegerField()
    colesterol = forms.IntegerField()
    triglicerido = forms.IntegerField()
    bilirrubina = forms.IntegerField()
    fecha = forms.DateField()
