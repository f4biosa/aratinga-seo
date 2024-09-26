import json
from datetime import datetime
from enum import Enum
from typing import Optional

from django.db import models
from django.utils.translation import gettext_lazy as _
from wagtail import VERSION as WAG_VERSION
from wagtail.admin.panels import FieldPanel
from wagtail.admin.panels import HelpPanel
from wagtail.admin.panels import MultiFieldPanel
from wagtail.contrib.settings.models import register_setting
from wagtail.fields import StreamField
from wagtail.images import get_image_model_string
from wagtail.images.models import AbstractImage
from wagtail.models import Page

from aratinga_seo import schemaorg
from aratinga_seo import settings
from aratinga_seo import utils
from aratinga_seo.blocks import OpenHoursBlock
from aratinga_seo.blocks import StructuredDataActionBlock


# Wagtail 3
if WAG_VERSION[0] == 3:
    from wagtail.contrib.settings.models import BaseSetting as BaseSiteSetting
# Wagtail 4+
else:
    from wagtail.contrib.settings.models import BaseSiteSetting


# Slug widget was added in Wagtail 5 and is required to properly generate slugs.
slug_field_kwargs = {}
if WAG_VERSION[0] >= 5:
    from wagtail.admin.widgets.slug import SlugInput

    slug_field_kwargs = {"widget": SlugInput}


class SeoType(Enum):
    ARTICLE = "article"
    WEBSITE = "website"