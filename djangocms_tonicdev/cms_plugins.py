# -*- coding: utf-8 -*-

from django.conf import settings

from cms.models import CMSPlugin
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from .models import TonicNotebookPluginModel
from .forms import TonicNotebookPluginAdminForm

from django.utils.translation import ugettext_lazy as _


class TonicNotebookPlugin(CMSPluginBase):
    form = TonicNotebookPluginAdminForm
    name = _('Notebook')
    module = _('Tonic')
    model = TonicNotebookPluginModel
    render_template = "djangocms_tonicdev/notebook.html"
    text_enabled = True

    def render(self, context, instance, placeholder):
        context['instance'] = instance
        return context

    def icon_src(self, instance):
        # //img.shields.io/badge/tonic-notebook-green.svg'
        return settings.STATIC_URL + 'djangocms_tonicdev/tonic-notebook-green.svg'

    def icon_alt(self, instance):
        return u'TonicNotebook: %s' % instance


plugin_pool.register_plugin(TonicNotebookPlugin)
