from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class HomeworkConfig(AppConfig):
    name = 'homework'
    verbose_name = _('homework')

    def ready(self):
        import homework.signals
