from dataclasses import fields
import email
from pyexpat import model
from django import forms 
from inicio.models import InformeSemanalModel, EncuestaModel, ContactenosModel


class FormularioDeInscripcion(forms.ModelForm):
    email = forms.EmailField(max_length=100, label='', help_text='', widget=forms.EmailInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'ingrese su email'}))
    
    class Meta:
        model = InformeSemanalModel
        fields = ['email']

class FormularioEncuesta(forms.ModelForm):
    respuesta = forms.CharField(label=EncuestaModel._meta.get_field('pregunta').get_default(), widget= forms.TextInput(attrs={'class': 'form-control form-control-sm'}))


    class Meta: 
        model = EncuestaModel
        fields = ['respuesta']

class FormularioContactenos(forms.ModelForm):
    nombre = forms.CharField(label='Nombre', widget= forms.TextInput(attrs={'class': 'form-control form-control-sm'}))
    email = forms.CharField(label='Email', widget= forms.EmailInput(attrs={'class': 'form-control form-control-sm'}))
    asunto = forms.CharField(label='Asunto', widget= forms.TextInput(attrs={'class': 'form-control form-control-sm'}))
    mensaje = forms.CharField(label='Mensaje', widget= forms.Textarea(attrs={'class': 'form-control form-control-sm', 'rows': 3}))

    class Meta:
        model = ContactenosModel
        fields = ['nombre', 'email', 'asunto', 'mensaje']
