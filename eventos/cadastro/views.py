from django.shortcuts import render
from .form import Inscrevase
from .models import Inscrito
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView

# Create your views here.

def cadastro(request):
	context = {}
	if request.method == 'POST':
		form = Inscrevase(request.POST)
		if form.is_valid():
			novo_inscrito = form.save()
			context['is_valid'] = True
			form = Inscrevase()

	else:
		form = Inscrevase()
	context['form'] = form
	template_name = 'cadastro.html'
	return render(request,template_name,context)

class Cadastro(CreateView):

	model = Inscrito
	template_name = 'cadastro.html'
	form_class = Inscrevase

class Dashboard(TemplateView):
	template_name = 'dashboard.html'
