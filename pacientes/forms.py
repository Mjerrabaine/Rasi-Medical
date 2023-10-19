from django import forms
from .models import Paciente

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = [
            'variable',
            'nombre',
            'edad',
            'cc',
            'genero',
            'estatura',
            'peso',
            'rh',
            #'dateTime',
        ]

        labels = {
            'variable' : 'Variable',
            'nombre' : 'Nombre',
            'edad' : 'Edad',
            'cc' : 'Cc',
            'genero' : 'Genero',
            'estatura' : 'Estatura',
            'peso' : 'Peso',
            'rh' : 'Rh',
            #'dateTime' : 'Date Time',
        }
