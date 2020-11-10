from django.apps import AppConfig
from django.db.models.signals import post_save
from django.utils.translation import ugettext_lazy as _

from .models import League
from .signals import push_new_leagues


class ContestConfig(AppConfig):
    name = 'Contest'
    verbose_name = _('contest')

    def ready(self):
        post_save.connect(push_new_leagues, sender=League, weak=False)