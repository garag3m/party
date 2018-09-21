from django.shortcuts import render
from .form import Inscrevase
from .models import Inscrito
from app.core import models
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView

from django.http import HttpResponse
from django.views.generic import View

from .utils import render_to_pdf
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


class MyInsc(TemplateView):

	template_name = 'cadastro/inscricao.html'

	def get_context_data(self, **kwargs):
		context = super(MyInsc, self).get_context_data(**kwargs)
		context['inscricao'] = Inscrito.objects.filter(usuario_id=self.request.user.id)
		return context

class GeneratePDF(View):
    def get(self, request, *args, **kwargs):
        template = get_template('invoice.html')
        context = {
            "invoice_id": 123,
            "customer_name": "John Cooper",
            "amount": 1399.99,
            "today": "Today",
        }
        html = template.render(context)
        pdf = render_to_pdf('invoice.html', context)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "Invoice_%s.pdf" %("12341231")
            content = "inline; filename='%s'" %(filename)
            download = request.GET.get("download")
            if download:
                content = "attachment; filename='%s'" %(filename)
            response['Content-Disposition'] = content
            return response
        return HttpResponse("Not found")