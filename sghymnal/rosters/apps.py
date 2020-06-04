from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class RostersConfig(AppConfig):
    name = "sghymnal.rosters"
    verbose_name = _("Rosters")
