# -*- coding: utf-8 -*-

from django.contrib import admin
from .models import TonicNotebookConfigModel


class TonicNotebookConfigAdmin(admin.ModelAdmin):
    pass

admin.site.register(TonicNotebookConfigModel, TonicNotebookConfigAdmin)
