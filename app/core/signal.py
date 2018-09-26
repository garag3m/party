from django.db.models.signals import pre_delete
from . import models

def deletar_negado(sender, instance, using, **kwargs):
    d = models.Evento()
    if d.finalizado == 0:
        print('fim')
    elif d.finalizado == 1:
        print('nao')
    elif d.finalizado == 2:
        print('acon')

    d.save()

pre_delete.connect(receiver=deletar_negado)
