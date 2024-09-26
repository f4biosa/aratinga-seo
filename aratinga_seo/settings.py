"""
Provide default Django settings.
"""

from django.conf import settings


# Title sitename separator. Default is em-dash.
DEFAULTS = {"ARATINGA_SEO_SEP": "—"}


def get(name: str):
    return getattr(settings, name, DEFAULTS[name])
