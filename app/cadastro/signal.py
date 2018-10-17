from django.db.models.signals import pre_delete, pre_save
from app.core import models


def edicao_invalida(sender, instance, **kwargs):
    edicao_atual =  models.Evento.objects.filter(edicao=1)
    for ed in edicao_atual:

        if instance.edicao <= ed.edicao:
            raise Exception("Edição invalida!")
    # if instance.edicao_anterior == None:
    #     raise Exception("Edição Invalida!")
pre_save.connect(edicao_invalida, sender=models.Evento)
