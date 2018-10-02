from django.apps import AppConfig


class CoreConfig(AppConfig):
    name = 'app.core'

    def ready(self):
        from . import signal
