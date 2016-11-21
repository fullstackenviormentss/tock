# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-16 13:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0016_project_profit_loss_account'),
    ]

    operations = [
        migrations.AddField(
            model_name='profitlossaccount',
            name='as_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='profitlossaccount',
            name='as_end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profitlossaccount',
            name='as_start_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]