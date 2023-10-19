from ..models import Paciente

def get_pacientes():
    queryset = Paciente.objects.all().order_by('-dateTime')[:10]
    return (queryset)

def create_activo(form):
    activo = form.save()
    activo.save()
    return ()