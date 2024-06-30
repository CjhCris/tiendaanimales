# forms.py
from django import forms
from .models import Usuario

class UsuarioForm(forms.ModelForm):

    class Meta:
        model = Usuario
        fields= ["usuario", "nombre", "apPaterno", "correo", "contraseña", "confirmar_contraseña", "rut", "edad"]