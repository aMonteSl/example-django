from django import forms
from .models import Contenido

class ContenidoForm(forms.ModelForm):
    class Meta:
        model = Contenido
        fields = ('clave', 'valor', )
                