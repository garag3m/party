import uuid
import datetime
from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone
from eventos.cadastro.models import Inscrito
# from .consultas import evento_finalizado, excluir_evento

# Create your models here.

class Noticia(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	titulo = models.CharField("Titulo",max_length=150)
	autor = models.CharField("Autor",max_length=100)
	texto = models.TextField("Sobre")
	data_public = models.DateTimeField("Publicado em",default=timezone.now)

	evento = models.ForeignKey('Evento', on_delete=models.CASCADE, related_name='noticias')

	def __str__(self):
		return self.titulo

	def publicado_em(self):
		self.data_public = timezone.now()
		self.save()

	class Meta:
		verbose_name = "Noticia"
		verbose_name_plural = "Noticias"
		db_table = "noticia"

class Evento(models.Model):

	STATUS = (
		(0,"Finalizado"),
		(1,"Não Finalizado"),
		(2,"Acontecendo")
	)

	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	nome = models.CharField("Nome do evento",max_length=150)
	finalizado = models.IntegerField(verbose_name="Status do evento",
		help_text='Marcar o campo referente ao estado atual do evento',
		choices = STATUS
	)
	descricao = models.TextField("Descrição")
	slug = models.SlugField(max_length=100)
	edicao = models.PositiveIntegerField(verbose_name='Edição',default=1)
	tema = models.CharField("Tema do evento",max_length=150)
	data = models.DateField("Inicio do evento",default=datetime.date.today)
	data_fim = models.DateField("Final do evento",default=datetime.date.today)

	def __str__(self):
		return self.nome

	def data_inicio(self):
		self.data = timezone.now()
		self.save()

	def clean(self):

		hoje = datetime.date.today()
		# evento = evento_finalizado(self.nome)
		# deletar_evento = excluir_evento(self.nome)

		if (self.data < hoje) or (self.data_fim < hoje):
			raise ValidationError('Data Invalida! Você não pode adicionar uma data que ja passou.')

		# elif evento == False:
		# 	raise ValidationError("Impossível alterar o evento!")

		# elif deletar_evento == True:
		# 	raise ValidationError("ok")


	class Meta:
		verbose_name = "Evento"
		verbose_name_plural = "Eventos"
		db_table = "evento"

class Foto(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    autor = models.CharField("Autor",max_length=100)
    descricao = models.CharField("Descrição",max_length=255)
    imagem = models.ImageField(upload_to='imagem',verbose_name="Imagem")

    galeria = models.ForeignKey("Galeria", on_delete=models.CASCADE, related_name='fotos')

    def __str__(self):
    	return self.autor

    class Meta:
    	verbose_name = "Foto"
    	verbose_name_plural = "Fotos"
    	db_table = "foto"

class Galeria(models.Model):

	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	evento = models.ForeignKey(Evento, on_delete=models.CASCADE, verbose_name="Evento", related_name='galerias')
	titulo = models.CharField("Titulo", max_length=100)

	def __str__(self):
		return self.titulo

	class Meta:
		verbose_name = "Galeria"
		verbose_name_plural = "Galerias"
		db_table = "galeria"
