# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-13 02:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('talent_portal', '0011_DOBfieldOptional'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_id', models.CharField(blank=True, max_length=10, null=True)),
                ('posted_by', models.CharField(blank=True, max_length=256, null=True)),
                ('title', models.CharField(blank=True, max_length=256, null=True)),
                ('description', models.CharField(blank=True, max_length=256, null=True)),
                ('target_exp', models.DecimalField(blank=True, decimal_places=2, max_digits=19, null=True)),
                ('min_salary', models.IntegerField(blank=True, null=True)),
                ('max_salary', models.IntegerField(blank=True, null=True)),
                ('salary_text', models.CharField(blank=True, max_length=256, null=True)),
                ('tag', models.CharField(blank=True, max_length=256, null=True)),
                ('functional_area', models.CharField(blank=True, max_length=256, null=True)),
                ('industry', models.CharField(blank=True, max_length=256, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='JobApplicant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('email', models.EmailField(max_length=70)),
                ('mobile', models.CharField(max_length=256)),
                ('resume_url', models.URLField(blank=True, null=True)),
                ('linkedin_url', models.URLField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('job', models.ManyToManyField(to='talent_portal.Job')),
            ],
        ),
    ]
