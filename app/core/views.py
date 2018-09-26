from django.shortcuts import render
from .models import Noticia, Evento, Galeria, Foto
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.db.models import Q
from app.cadastro import models
from django.views.generic.edit import CreateView

from . import form

# Create your views here.

class IndexView(TemplateView):

	template_name = 'core/index.html'

	def get_context_data(self, **kwargs):
		context = super(IndexView, self).get_context_data(**kwargs)
		context['noticias'] = Noticia.objects.all()
		return context

class BuscarEventoList(TemplateView):

	def post(self, request, *args, **kwargs):
		buscar = request.POST.get('buscar_event','')
		eventos = Evento.objects.filter(Q(nome__contains=buscar) | Q(data__contains=buscar))
		if eventos:
			print("OK")
			return render(request, 'core/detalhes_list.html', {'eventos': eventos})
		else:
			print('erro')
			return render(request, 'core/detalhes_list.html', {'msn': 'Erro! tente digitar algo!!'})

class BuscarEvento(DetailView):

	model = Evento
	template_name = 'core/detalhe.html'

class VisualizaAlbum(TemplateView):

	template_name = 'core/album.html'

	def get_context_data(self, **kwargs):
		context = super(VisualizaAlbum, self).get_context_data(**kwargs)

		context['fotos'] = Foto.objects.filter()
		return context

class CadastraEvento(CreateView):

	model = Evento
	template_name = 'cadastro.html'
	form_class = form.RegistrarEvento
