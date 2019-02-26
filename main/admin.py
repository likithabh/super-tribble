from django.contrib import admin
from .models import Mlblogger
from tinymce.widgets import TinyMCE
from django.db import models

class MlbloggerAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Title/date", {"fields": ["mlblogger_title", "mlblogger_published"]}),
        ("Content", {"fields":["mlblogger_content"]})
    ]

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()}
    }

admin.site.register(Mlblogger, MlbloggerAdmin)
