from django.db import models
from variables.models import Variable

class Paciente(models.Model):
    variable = models.ForeignKey(Variable, on_delete=models.CASCADE, default=None)
    nombre = models.CharField(max_length=50)
    edad = models.FloatField(null=True, blank=True, default=None)
    cc = models.CharField(max_length=50)
    genero = models.CharField(max_length=50)
    estatura = models.FloatField(null=True, blank=True, default=None)
    peso = models.FloatField(null=True, blank=True, default=None)
    rh = models.CharField(max_length=3)
    dateTime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s %s' % (self.value, self.unit)