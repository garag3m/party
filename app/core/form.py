from django import forms
from app.cadastro.models import Inscrito

class InscreveEvento(forms.ModelForm):

    hidden = forms.CharField(widget=forms.HiddenInput())

    class Meta:

        model = Inscrito
        fields = ['hidden']
