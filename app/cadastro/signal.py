from django.db.models.signals import pre_delete, pre_save
from app.core import models


def edicao_invalida(sender, instance, **kwargs):
    edicao_atual =  models.Evento.objects.all()
    for ed in edicao_atual:

        if (instance.nome == ed.nome) and (instance.edicao > ed.edicao):
            raise Exception("Edição invalida!")
pre_save.connect(edicao_invalida, sender=models.Evento)
