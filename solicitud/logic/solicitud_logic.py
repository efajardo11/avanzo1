from ..models import Solicitud

def get_solicitud():
    queryset = Solicitud.objects.all()
    return (queryset)

def create_solicitud(form):
    solicitud = form.save()
    solicitud.save()
    return ()