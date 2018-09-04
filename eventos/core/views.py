from django.shortcuts import render
from .models import Noticia,Evento, Galeria, Foto
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.db.models import Q

# Create your views here.

class IndexView(TemplateView):

	template_name = 'index.html'

	def get_context_data(self, **kwargs):
		context = super(IndexView, self).get_context_data(**kwargs)
		context['noticias'] = Noticia.objects.all()
		return context

class BuscarEventoList(TemplateView):

	def post(self, request, *args, **kwargs):
		buscar = request.POST['buscar_event']
		eventos = Evento.objects.filter(Q(nome__contains=buscar) | Q(data__contains=buscar))
		if eventos:
			print("OK")
			return render(request, 'detalhes_list.html', {'eventos': eventos})
		else:
			print('erro')
			return render(request, 'detalhes_list.html', {'msn': 'Erro! tente digitar algo!!'})

class BuscarEvento(DetailView):

	model = Evento
	template_name = 'detalhe.html'

class VisualizaAlbum(TemplateView):

	template_name = 'album.html'

	def get_context_data(self, **kwargs):
		context = super(VisualizaAlbum, self).get_context_data(**kwargs)

		context['fotos'] = Foto.objects.filter()
		return context
