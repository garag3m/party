from django.shortcuts import render, redirect
from .form import Inscrevase
from .models import Inscrito
from app.core import models
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView

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
        context['certificado'] = Inscrito.objects.filter(usuario_id=self.request.user.id)
        return context

class MyInsc(TemplateView):

	template_name = 'cadastro/inscricao.html'

	def get_context_data(self, **kwargs):
		context = super(MyInsc, self).get_context_data(**kwargs)
		context['inscricao'] = Inscrito.objects.filter(usuario_id=self.request.user.id)
		return context

	def post(self, request, *args, **kwargs):

		u = self.request.POST.get("envia","")
		print(u)

		c = Inscrito.objects.filter(usuario_id=self.request.user.id)
		c.evento=u
		c.save()
		return c

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
