from django import forms
from .models import solicitante

class solicitanteForm(forms.ModelForm):
    class Meta:
        model = solicitante
        fields = [
            'empresa',
            'pago',
        ]

        labels = {
            'empresa' : 'Empresa',
            'pago' : 'Pago',
        }