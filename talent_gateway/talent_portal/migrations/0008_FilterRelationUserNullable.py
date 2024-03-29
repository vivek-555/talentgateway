# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-29 15:11
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('talent_portal', '0007_FilterTableTypeFieldAdded'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filter',
            name='user',
            field=models.ManyToManyField(blank=True, null=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
