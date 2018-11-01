from django.shortcuts import render, redirect, get_object_or_404, render_to_response

from .form import Inscrevase, RegistrarEvento, PublicarFotos, AtividadeForm

from .models import EmitirCertificado, Inscrito, Atividade
from app.core import models
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from django.urls import reverse_lazy

from django.http import HttpResponse
from django.views.generic import View
from django.template.loader import get_template
from .utils import render_to_pdf
from django.template import Context

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
	template_name = 'cadastro/cadastro.html'
	return render(request,template_name,context)

# class Cadastro(CreateView):

# 	model = Inscrito
# 	template_name = 'cadastro.html'
# 	form_class = Inscrevase

class Dashboard(TemplateView):

	template_name = 'cadastro/dashboard.html'

	def get_context_data(self, **kwargs):
		context = super(Dashboard, self).get_context_data(**kwargs)

		context['lista'] = models.Evento.objects.all()

		context['autoriza'] = EmitirCertificado.objects.filter(inscrito_id=self.request.user.id)

		return context

class MyInsc(TemplateView):

	template_name = 'cadastro/inscricao.html'

	def get_context_data(self, **kwargs):
		context = super(MyInsc, self).get_context_data(**kwargs)
		context['inscricao'] = EmitirCertificado.objects.filter(inscrito_id=self.request.user.id)
		return context

class GeneratePDF(View):
    def get(self, request, *args, **kwargs):
        nome = Inscrito.objects.filter(usuario_id=self.request.user.id)
        template = get_template('pdf/certificado.html')
        for n in nome:
            context = {
                "nome": n.nome,
                "curso": n.idade,
                "carga_h": n.evento
            }
        html = template.render(context)
        pdf = render_to_pdf('pdf/certificado.html', context)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = 'Invoice_%s.pdf' %("12341231")
            content = "inline; filename='%s'" %(filename)
            download = request.GET.get("download")
            if download:
                content = "attachment; filename='%s'" %(filename)
            response['Content-Disposition'] = content
            return response
        return HttpResponse("Não existe")

class CadastraEvento(CreateView):

	model = models.Evento
	template_name = 'admin/cadastro_evento.html'
	form_class = RegistrarEvento
	success_url = reverse_lazy('cadastro:cadastro-evento')

class AlterarEvento(UpdateView):

    model = models.Evento
    template_name = 'admin/alterar_evento.html'
    success_url = reverse_lazy('cadastro:dashboard')
    fields = ['nome', 'finalizado', 'descricao', 'edicao', 'tema', 'carga_h', 'data', 'data_fim']

def evento_delete(request, pk, template_name='admin/excluir_retorno.html'):
    evento= get_object_or_404(models.Evento, pk=pk)
    if request.method=='POST':
        evento.delete()
        return redirect('cadastro:dashboard')
    return render(request, template_name, {'object':evento})

class RetornoEvento(TemplateView):

    template_name = 'admin/alterar_retorno.html'

class ListaUsuarios(CreateView):

	model = EmitirCertificado
	template_name = 'admin/usuario.html'
	fields = ['qt_falta','evento','emitir_cert','inscrito']
	success_url = reverse_lazy('cadastro:dashboard')

def erro(request):
	
	return render_to_response("cadastro/erro.html")

class PublicarFotos(CreateView):

	model = models.Evento
	template_name = 'admin/cadastro_evento.html'
	form_class = PublicarFotos
	success_url = reverse_lazy('cadastro:dashboard')

class AtividadeEvento(CreateView):

	model = Atividade
	template_name = 'admin/cria_atividade.html'
	form_class = AtividadeForm
	success_url = reverse_lazy('cadastro:dashboard')