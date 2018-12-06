from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from participantes.models import Estado, Municipio


class SignUpForm(UserCreationForm):
    curp = forms.CharField(max_length=50, required=False)
    nombre = forms.CharField(max_length=30, required=False)
    apellido_paterno = forms.CharField(max_length=30, required=False)
    apellido_materno = forms.CharField(max_length=30, required=False)
    estado = forms.ModelChoiceField(queryset=Estado.objects.all())
    municipio = forms.ModelChoiceField(queryset=Municipio.objects.all())
    telefono = forms.CharField(max_length=20, required=False)
    email = forms.EmailField(max_length=254, required=False)
    ocupacion = forms.CharField(max_length=100, required=False)
    foto = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = (
            'curp',
            'nombre',
            'apellido_paterno',
            'apellido_materno',
            'estado',
            'municipio',
            'telefono',
            'ocupacion',
            'username',
            'email',
            'password1',
            'password2',
            'foto',
        )