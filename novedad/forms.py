from django import forms
from .models import novedad

class novedadForm(forms.ModelForm):
    class Meta:
        model = novedad
        fields = [
            'descripcion',
        ]

        labels = {
            'descripcion' : 'Descripcion',
        }