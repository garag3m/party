from django.shortcuts import render
from .models import Noticia, Evento, Galeria, Foto
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.db.models import Q
from app.cadastro import models
from django.views.generic.edit import CreateView

from django.http import HttpResponseRedirect

# Create your views here.

class IndexView(TemplateView):

	template_name = 'core/index.html'

	def get_context_data(self, **kwargs):
		context = super(IndexView, self).get_context_data(**kwargs)
		context['noticias'] = Noticia.objects.all()
		return context

class BuscarEventoList(TemplateView):

	template_name = 'core/detalhes_list.html'
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

		gal = Galeria.objects.filter(evento_id=self.kwargs['pk'])
		context['fotos'] = Foto.objects.filter(galeria_id=gal[0])
		return context

# class GaleriaDeFotos(CreateView):

# class PublicarFotos(CreateView):

# 	model = models.Evento
# 	template_name = 'admin/cadastro_evento.html'
# 	form_class = form.PublicarFotos
# 	success_url = reverse_lazy('cadastro:cadastro-evento')

def inscrevase(request, id):

	event = Evento.objects.get(id=id)

	ins = models.Inscrito.objects.get(usuario=request.user.id)
	
	ins.evento = event
	ins.save()

	return HttpResponseRedirect('/cadastro/dashboard/')
