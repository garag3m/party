from django.db.models.signals import pre_delete, pre_save
from . import models
from app.cadastro import views


# def edicao_invalida(sender, instance, **kwargs):
#     edicao_atual =  models.Evento.objects.filter(edicao=1)
#     if instance.edicao > edicao_atual.edicao:
#         print("ok")
#     # if instance.edicao_anterior == None:
#     #     raise Exception("Edição Invalida!")
# pre_save.connect(edicao_invalida, sender=models.Evento)

def deletar_evento(sender, instance, **kwargs):

    if (instance.finalizado == "Finalizado") or (instance.finalizado == "Acontecendo"):
        raise Exception("Impossivel excluir evento!")
    # elif instance.finalizado == "Não Finalizado":
    #     exclui = models.Evento.objects.filter(finalizado="Não Finalizado").delete()
    #     exclui.save()

pre_delete.connect(deletar_evento, sender=models.Evento)
