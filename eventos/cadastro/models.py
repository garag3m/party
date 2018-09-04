import uuid
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

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

	def __str__(self):
		return self.nome

	class Meta:
		verbose_name = "Inscrito"
		verbose_name_plural = "Inscritos"
		db_table = 'inscrito'
