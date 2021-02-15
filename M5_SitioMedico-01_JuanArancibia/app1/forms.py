import datetime

from django import forms
from django.core import validators
from django.core.exceptions import ValidationError


class FormularioBusqueda(forms.Form):
    Rut = forms.CharField(
            validators = [
                validators.MinLengthValidator( 9, 
						    "El RUN no puede tener menos de 9 caracteres"),
                        validators.MaxLengthValidator( 10, 
						    "El RUN no puede tener mas de 10 caracteres") ]) 
    contra = forms.CharField()
             