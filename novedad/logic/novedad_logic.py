from ..models import novedad

def get_novedad():
    queryset = novedad.objects.all()
    return (queryset)

def create_novedad(form):
    novedad = form.save()
    novedad.save()
    return ()