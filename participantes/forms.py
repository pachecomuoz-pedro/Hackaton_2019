from django import forms
from .models import Participante

class FormParticipante(forms.ModelForm):

    class Meta:
        model = Participante
        fields = ('curp','nombre','apellido_paterno','apellido_materno','estado','municipio','telefono','correo','ocupacion','foto')
