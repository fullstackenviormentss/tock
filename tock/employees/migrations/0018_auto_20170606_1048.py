# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-06-06 14:48
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0017_auto_20161116_1535'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdata',
            name='alt_work_schedule',
            field=models.BooleanField(default=False, verbose_name='Alternate Work Schedule'),
        ),
        migrations.AddField(
            model_name='userdata',
            name='authorized_hours',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), default=[40], size=None, verbose_name='Authorized Hours'),
        ),
    ]