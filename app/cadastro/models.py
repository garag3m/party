import uuid
from django.utils import timezone
from django.contrib.auth.models import User
from app.core.models import Evento
from django.db import models

# Create your models here.

class Inscrito(models.Model):

	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	nome = models.CharField(max_length=100)
	idade = models.PositiveIntegerField()
	cidade = models.CharField(max_length=100)
	uf = models.CharField(max_length=4)
	cpf = models.PositiveIntegerField()
	rg = models.PositiveIntegerField()
	telefone = models.CharField(max_length=15)
	usuario = models.OneToOneField(User,related_name='inscritos',on_delete=models.CASCADE)
	evento = models.ForeignKey(Evento,on_delete=models.CASCADE, null=True, blank=True)

	def __str__(self):
		return self.nome

	class Meta:
		verbose_name = "Inscrito"
		verbose_name_plural = "Inscritos"
		db_table = 'inscrito'

class Responsavel(models.Model):

	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	usuario = models.OneToOneField(User,related_name='responsaveis',on_delete=models.CASCADE)
	evento = models.OneToOneField(Evento,on_delete=models.CASCADE)

	def __str__(self):
		return "%s - %s" %(self.usuario.email, self.evento)

	class Meta:
		verbose_name = "Responsavel"
		verbose_name_plural = "Responsaveis"
		db_table = 'responsavel'

class EmitirCertificado(models.Model):

	AUTORIZAR = (
		(0,"Autorizo"),
		(1,"Não autorizo")
	)
	inscrito = models.OneToOneField(Inscrito, on_delete=models.CASCADE)

	qt_falta = models.CharField("Quantidade de faltas",max_length=3)
	emitir_cert = models.IntegerField(verbose_name="Emissão do certificado",
		help_text='Deseja autorizar a emissão do certificado para o respectivo usuário',
		choices = AUTORIZAR
	)

	def __str__(self):
		return str(self.inscrito)