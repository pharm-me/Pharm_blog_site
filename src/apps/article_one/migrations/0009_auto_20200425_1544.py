# Generated by Django 3.0.5 on 2020-04-25 12:44

import datetime

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ('article_one', '0008_auto_20200425_1210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlecontent',
            name='article_one_time',
            field=models.DateField(default=datetime.datetime(2020, 4, 25, 12, 44, 42, 443615)),
        ),
    ]
