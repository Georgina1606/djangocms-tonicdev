# -*- coding: utf-8 -*-

from django import forms
from django.forms.models import ModelForm

from .models import TonicNotebookPluginModel

from django.utils.translation import ugettext_lazy as _


class TonicNotebookPluginAdminForm(ModelForm):

    class Meta:
        model = TonicNotebookPluginModel
        exclude = ()

    def __init__(self, *args, **kwargs):
        super(TonicNotebookPluginAdminForm, self).__init__(*args, **kwargs)
