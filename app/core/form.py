from django import forms
from app.cadastro.models import Inscrito

class InscreveEvento(forms.ModelForm):

    hidden = forms.CharField(widget=forms.HiddenInput())

    class Meta:

        model = Inscrito
        fields = ['hidden']

class RegistrarEvento(forms.ModelForm):

    nome = forms.CharField(label='Nome',widget=forms.TextInput(
		attrs={'class':'form-control','placeholder':'Nome completo do aluno'}))
