# Generated by Django 2.1.7 on 2019-02-23 20:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20190224_0220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mlblogger',
            name='mlblogger_published',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 24, 2, 25, 1, 473261), verbose_name='date published'),
        ),
    ]