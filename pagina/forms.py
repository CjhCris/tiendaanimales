# forms.py
from django import forms
from .models import Usuario

class RegistroForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['usuario','nombre', 'apellido', 'correo', 'rut', 'contraseña', 'edad']

