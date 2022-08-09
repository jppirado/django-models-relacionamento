
from tkinter import Widget
from peopleApp.models import People , Contato
from django.forms import ModelForm
from django import forms


class PeopleForm(ModelForm):
    data_nascimento = forms.DateField(
        widget = forms.TextInput(
            attrs={ "type" : "date" }
        )
    )
    class Meta:
        model = People
        fields = ( 'nome_completo' , 'data_nascimento' , 'ativa')
 
class ContatoForm( ModelForm):
    class Meta:
        model = Contato
        fields = ('nome','email','telefone') 