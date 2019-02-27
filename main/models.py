from django.db import models
from datetime import datetime

class MlbloggerCategory(models.Model):
    mlblogger_category = models.CharField(max_length=200)
    category_summary = models.CharField(max_length=200)
    category_slug = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.mlblogger_category

class MlbloggerSeries(models.Model):
    mlblogger_series = models.CharField(max_length=200)
    mlblogger_category = models.ForeignKey(MlbloggerCategory, default=1, verbose_name="category", on_delete=models.SET_DEFAULT)
    series_summary = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "Series"

    def __str__(self):
        return self.mlblogger_series
     

# Create your models here.
class Mlblogger(models.Model):
    mlblogger_title = models.CharField(max_length=200)
    mlblogger_content = models.TextField()
    mlblogger_published = models.DateTimeField("date published", default=datetime.now())

    mlblogger_series = models.ForeignKey(MlbloggerSeries, default=1, verbose_name="Series", on_delete=models.SET_DEFAULT)
    
    mlblogger_slug = models.CharField(max_length=200, default=1)
    def __str__(self):
        return self.mlblogger_title
