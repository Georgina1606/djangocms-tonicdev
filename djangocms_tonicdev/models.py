# -*- coding: utf-8 -*-

import json

from cms.models import CMSPlugin
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from cms.utils.compat.dj import python_2_unicode_compatible


@python_2_unicode_compatible
class TonicNotebookConfigModel(models.Model):

    name = models.CharField('Name',
        null=False,
        blank=False,
        help_text=_(u'Config name'),
        max_length=32,
    )

    node_version = models.CharField('Node version',
        null=True,
        blank=True,
        help_text=_(u'Provide a semver range that the node engine should satisfy, e.g. 0.12.x or > 4.0.0'),
        max_length=32,
    )

    script_block = models.CharField('Script block',
        null=False,
        blank=False,
        default='js',
        help_text=_(u'Script block'),
        max_length=32,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Tonic notebook config')
        verbose_name_plural = _('Tonic notebook configs')


@python_2_unicode_compatible
class TonicNotebookPluginModel(CMSPlugin):

    config = models.ForeignKey(TonicNotebookConfigModel,
        null=False,
        blank=False,
        verbose_name=_('Notebook config')
    )

    name = models.CharField('Name',
        null=True,
        blank=True,
        help_text=_(u'Name (optional)'),
        max_length=32,
    )

    code = models.TextField('Source code',
        blank=False,
        default='',
        help_text=_(u'Source code'),
    )

    node_version = models.CharField('Node version',
        null=True,
        blank=True,
        help_text=_(u'Provide a semver range that the node engine should satisfy, e.g. 0.12.x or > 4.0.0'),
        max_length=32,
    )

    readonly = models.BooleanField('Readonly',
        blank=False,
        default=False,
        help_text=_(u'Create a notebook that can not be edited or run'),
    )

    def script_block(self):
        return self.config.script_block
        
    def get_node_version(self):
        return self.config.node_version if self.config.node_version else self.node_version
        
    def ident(self):
        return self.name if self.name else str(self.id)
        
    def variable_name(self):
        return 'djangocms_tonicdev_' + self.ident()
        
    def opts(self):
        result = {
            'ident': self.ident(),
            'variable_name': self.variable_name(),
            'node_version': self.get_node_version(),
            'readonly': self.readonly,
        }
        return json.dumps(result)

    def __str__(self):
        return _(u'TonicNotebook %(id)s') % {'id': self.id}
