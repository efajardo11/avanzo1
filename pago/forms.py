from django import forms
from .models import pago

class pagoForm(forms.ModelForm):
    class Meta:
        model = pago
        fields = [
            'valor',
            'descuento',
            'descripcion',
        ]

        labels = {
            'valor' : 'Valor',
            'descuento' : 'Descuento',
            'descripcion' : 'Descripcion',
        }