from ..models import Activo

def get_Activos():
    queryset = Activo.objects.all().order_by('-dateTime')[:10]
    return (queryset)

def create_Activo(form):
    Activo = form.save()
    Activo.save()
    return ()