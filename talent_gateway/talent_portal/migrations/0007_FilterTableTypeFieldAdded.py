# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-28 16:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('talent_portal', '0006_FilterTableAdded'),
    ]

    operations = [
        migrations.AddField(
            model_name='filter',
            name='type',
            field=models.CharField(choices=[('Global', 'Global'), ('Local', 'Local')], default='Local', max_length=10),
        ),
    ]