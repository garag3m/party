from django.db.models.signals import pre_delete, pre_save
from . import models


# def edicao_invalida(sender, instance, **kwargs):
#     # if instance.edicao_anterior == None:
#     #     raise Exception("Edição Invalida!")
#     pass
#
# pre_save.connect(edicao_invalida, sender=models.Evento)

def deletar_evento(sender, instance, **kwargs):

    if (instance.finalizado == 0) or (instance.finalizado == 2):
        raise Exception("Impossivel excluir evento!")

pre_delete.connect(deletar_evento, sender=models.Evento)
