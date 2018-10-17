from django.apps import AppConfig


class CadastroConfig(AppConfig):
    name = 'app.cadastro'

    def ready(self):
        from . import signal
