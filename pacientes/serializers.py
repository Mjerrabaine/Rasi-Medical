from rest_framework import serializers
from . import models


class PacienteSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'variable','nombre',  'edad', 'cc', 'genero', 'estatura', 'peso', 'rh',)
        model = models.Paciente