from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class ContestConfig(AppConfig):
    name = 'Contest'
    verbose_name = _('contest')

    def ready(self):
        import Contest.signals