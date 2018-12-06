from django import forms
from .models import Equipo

class FormEquipo(forms.ModelForm):

	class Meta:
		model = Equipo
		fields = ('nombre_equipo','vertical','participante_1','participante_2','participante_3','participante_4')