# -*- coding: utf-8 -*-
from django import forms
from .models import Inscrito

from app.core import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Inscrevase(forms.Form):

	nome = forms.CharField(label='Nome',widget=forms.TextInput(
		attrs={'class':'form-control','placeholder':'Nome completo do aluno'}))

	email = forms.EmailField(label='E-mail',widget=forms.EmailInput(
		attrs={'class':'form-control','placeholder':'E-mail do aluno'}))

	senha = forms.CharField(label='Senha',widget=forms.PasswordInput(
		attrs={'class':'form-control','placeholder':'Digite uma senha'}))

	idade = forms.CharField(label='Idade',widget=forms.TextInput(
		attrs={'class':'form-control','placeholder':'Sua idade'}))

	cidade = forms.CharField(label="Cidade",widget=forms.TextInput(
		attrs={'class':'form-control','placeholder':'Cidade do aluno'}))

	uf = forms.CharField(label="UF",widget=forms.TextInput(
		attrs={'class':'form-control','placeholder':'Estado'}))

	cpf = forms.CharField(label="CPF",widget=forms.TextInput(
		attrs={'class':'form-control','placeholder':'CPF do aluno'}))

	rg = forms.CharField(label="RG",widget=forms.TextInput(
		attrs={'class':'form-control','placeholder':'RG do aluno'}))

	telefone = forms.CharField(label="Telefone",widget=forms.TextInput(
		attrs={'class':'form-control','placeholder':'Seu telefone'}))

	def clean_email(self):

		email = self.cleaned_data['email']
		if User.objects.filter(email=email).exists():
			raise forms.ValidationError("Já existe um e-mail com este nome!")
		return email

	def clean_cpf(self):

		cpf = self.cleaned_data['cpf']
		if User.objects.filter(username=cpf).exists():
			raise forms.ValidationError("Já existe um CPF cadastrado!")
		return cpf

	def save(self):

		nome = self.cleaned_data.get('nome')
		email = self.cleaned_data.get('email')
		senha = self.cleaned_data.get('senha')
		idade = self.cleaned_data.get('idade')
		cidade = self.cleaned_data.get('cidade')
		uf = self.cleaned_data.get('uf')
		cpf = self.cleaned_data.get('cpf')
		rg = self.cleaned_data.get('rg')
		telefone = self.cleaned_data.get('telefone')

		user = User.objects.create_user(
			password=senha,
			username=cpf,
			email=email
		)
		user.save()
		novo_inscrito = Inscrito(
			nome = nome,
			idade = idade,
	        cidade = cidade,
	        uf = uf,
	        cpf = cpf,
	        rg = rg,
	        telefone = telefone,
	        usuario_id=user.id,
	    )
		novo_inscrito.save()
		return novo_inscrito

class RegistrarEvento(forms.ModelForm):

    class Meta:
    	model = models.Evento
    	fields = ['nome', 'finalizado','descricao','edicao','tema','carga_h','data','data_fim']
