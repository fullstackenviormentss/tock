# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-03-14 19:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hours', '0029_merge_20170227_1725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timecardobject',
            name='grade',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='employees.EmployeeGrade'),
        ),
    ]