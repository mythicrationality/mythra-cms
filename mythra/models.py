from cms.models.pluginmodel import CMSPlugin
from cms.models.pagemodel import Page
from django.db import models
from django.utils.translation import ugettext_lazy as _


class IntroQuote(CMSPlugin):
    title = models.CharField(blank=True, verbose_name=_("title"), max_length=255)
    quote = models.TextField(blank=True, verbose_name=_("quote"))
    page = models.ForeignKey(Page, on_delete=models.CASCADE, null=True, blank=True, verbose_name=_("page"))


class Incantation(CMSPlugin):
    text = models.TextField(blank=True, verbose_name=_("text"))
