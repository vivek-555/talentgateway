# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-12 12:05
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('talent_portal', '0001_CustomerModelAdded'),
    ]

    operations = [
        migrations.CreateModel(
            name='Colleges',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('alias', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('name', models.CharField(max_length=256)),
                ('value', models.CharField(max_length=256)),
            ],
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='phone',
            new_name='mobile',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='company_name',
        ),
        migrations.AddField(
            model_name='customer',
            name='additional_college',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='additional_completion_year',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='additional_course',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='additional_degree',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='current_company',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='current_designation',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='current_exprience',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=19, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='current_functional_area',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='current_location',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='current_salary',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='dob',
            field=models.DateField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='customer',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='F', max_length=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customer',
            name='industry',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='notice_period',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='pg_college',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='pg_completion_year',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='pg_course',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='pg_degree',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='preferred_functional_area',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='preferred_industry',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='preferred_location',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='preferred_salary',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='primary_skills',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='resume_text',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='resume_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='secondary_email',
            field=models.EmailField(blank=True, max_length=70, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='secondary_mobile',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='secondary_skills',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='total_experience',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=19, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='ug_college',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='ug_completion_year',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='ug_course',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='ug_degree',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]