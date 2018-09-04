from django.contrib import admin
from .models import Foto, Noticia, Evento, Galeria

# Register your models here.
admin.site.site_header = "Sistema de Eventos"

class EventosAdmin(admin.ModelAdmin):

	list_display = ['nome','finalizado','slug','tema','data','data_fim']
	search_fields = ['nome','slug']
	prepopulated_fields = {'slug': ('nome',)}


class FotosAdmin(admin.ModelAdmin):

	list_display = ['autor','descricao','imagem','galeria']
	search_fields = ['autor']


class NoticiasAdmin(admin.ModelAdmin):

	list_display = ['titulo','autor','data_public']
	search_fields = ['titulo','autor']

class GaleriaAdmin(admin.ModelAdmin):

	list_display = ['titulo']

admin.site.register(Evento,EventosAdmin)
admin.site.register(Foto,FotosAdmin)
admin.site.register(Noticia,NoticiasAdmin)
admin.site.register(Galeria,GaleriaAdmin)
