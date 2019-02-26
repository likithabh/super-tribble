from django.db import models
from datetime import datetime

# Create your models here.
class Mlblogger(models.Model):
    mlblogger_title = models.CharField(max_length=200)
    mlblogger_content = models.TextField()
    mlblogger_published = models.DateTimeField("date published", default=datetime.now())

    def __str__(self):
        return self.mlblogger_title
