from ..models import solicitante

def get_solicitante():
    queryset = solicitante.objects.all()
    return (queryset)

def create_solicitante(form):
    solicitante = form.save()
    solicitante.save()
    return ()