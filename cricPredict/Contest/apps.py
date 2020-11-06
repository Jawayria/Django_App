from django.apps import AppConfig


class ContestConfig(AppConfig):
    name = 'Contest'

    def ready(self):
        import Contest.signals
