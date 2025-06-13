from django import forms
from .models import Comuna

class ComunaForm(forms.ModelForm):
    class Meta:
        model = Comuna
        fields = ['nombre', 'cantidad_habitantes', 'vulnerabilidad', 'fecha_fundacion']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'cantidad_habitantes': forms.NumberInput(attrs={'class': 'form-control', 'min': 0}),
            'vulnerabilidad': forms.NumberInput(attrs={
                'class': 'form-control', 'step': '0.001', 'min': 0, 'max': 1
            }),
            'fecha_fundacion': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

