# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2017-01-02 14:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kw_webapp', '0020_frequentlyaskedquestion'),
    ]

    operations = [
        migrations.AddField(
            model_name='userspecific',
            name='critical',
            field=models.BooleanField(default=False),
        ),
    ]
