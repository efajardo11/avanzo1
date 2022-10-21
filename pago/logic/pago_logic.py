from ..models import pago

def get_pago():
    queryset = pago.objects.all()
    return (queryset)

def create_pago(form):
    pago = form.save()
    pago.save()
    return ()