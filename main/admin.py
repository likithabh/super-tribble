from django.contrib import admin
from .models import Mlblogger, MlbloggerSeries, MlbloggerCategory
from tinymce.widgets import TinyMCE
from django.db import models

class MlbloggerAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Title/date", {"fields": ["mlblogger_title", "mlblogger_published"]}),
        ("URL", {"fields":["mlblogger_slug"]}),
        ("Series", {"fields":["mlblogger_series"]}),
        ("Content", {"fields":["mlblogger_content"]})
    ]

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()}
    }

admin.site.register(MlbloggerSeries)

admin.site.register(MlbloggerCategory)

admin.site.register(Mlblogger, MlbloggerAdmin)