# Generated by Django 3.0.5 on 2020-04-19 11:41

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0002_auto_20200417_2142'),
    ]

    operations = [
        migrations.AddField(
            model_name='articlepreview',
            name='article_1',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='articlepreview',
            name='article_2',
            field=models.TextField(blank=True, null=True),
        ),
    ]
