import uuid
from django.utils import timezone
from django.contrib.auth.models import User
from app.core.models import Evento
from django.db import models

from django.conf import settings

from django.contrib.auth.models import AbstractUser

# Create your models here.
class MyUser(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

class Inscrito(models.Model):

	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	nome = models.CharField(max_length=100)
	idade = models.PositiveIntegerField()
	cidade = models.CharField(max_length=100)
	uf = models.CharField(max_length=4)
	cpf = models.PositiveIntegerField()
	rg = models.PositiveIntegerField()
	telefone = models.CharField(max_length=15)
	usuario = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='inscritos',on_delete=models.CASCADE)
	evento = models.ForeignKey(Evento,on_delete=models.CASCADE, null=True, blank=True)

	def __str__(self):
		return "%s - CPF nº %s" %(self.nome, self.cpf)

	class Meta:
		verbose_name = "Inscrito"
		verbose_name_plural = "Inscritos"
		db_table = 'inscrito'

class Responsavel(models.Model):

	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	usuario = models.OneToOneField(settings.AUTH_USER_MODEL,related_name='responsaveis',on_delete=models.CASCADE)
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
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    inscrito = models.ForeignKey(Evento, on_delete=models.CASCADE)
    qt_falta = models.CharField("Quantidade de faltas",max_length=3)

    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    emitir_cert = models.IntegerField(verbose_name="Emissão do certificado",
        choices = AUTORIZAR
    )

	def __str__(self):
		return str(self.inscrito)

class Atividade(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    tipo = models.CharField("Tipo", max_length=255)
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    ministrante = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    titulo = models.CharField("Titulo", max_length=255)
    qt_inscritos = models.PositiveIntegerField(verbose_name="Quantidade de inscritos")
    descricao = models.TextField("Descrição")
    data = models.DateField("Data",default=datetime.date.today)
    local = models.CharField("Local", max_length=255)
    carga_h = models.PositiveIntegerField(verbose_name="Duração")

    def __str__(self):
        return "%s - Evento: %s" %(str(self.ministrante.first, self.evento.nome))
