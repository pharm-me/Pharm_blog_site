# Generated by Django 3.0.5 on 2020-05-02 19:03

import datetime

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ('article_one', '0009_auto_20200425_1544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlecontent',
            name='article_one_time',
            field=models.DateField(default=datetime.datetime(2020, 5, 2, 19, 3, 40, 563586)),
        ),
    ]
