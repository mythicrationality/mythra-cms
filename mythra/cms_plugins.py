from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _

from .models import IntroQuote, Incantation

@plugin_pool.register_plugin
class IntroQuotePlugin(CMSPluginBase):
    model = IntroQuote
    name = _("Introduction Quote")
    render_template = "_intro_quote.html"
    cache = False

    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        return context


@plugin_pool.register_plugin
class IncantationPlugin(CMSPluginBase):
    model = Incantation
    name = _("Incantation")
    render_template = "_incantation.html"
    cache = False

    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        return context
