# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-15 21:36
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0011_employeegrade'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employeegrade',
            name='g_end_date',
        ),
        migrations.AlterField(
            model_name='employeegrade',
            name='employee',
            field=models.ForeignKey(help_text='Please select from existing employees.', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='employeegrade',
            name='g_start_date',
            field=models.DateField(help_text='Please enter a start date for this grade.'),
        ),
        migrations.AlterField(
            model_name='employeegrade',
            name='grade',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10'), (11, '11'), (12, '12'), (13, '13'), (14, '14'), (15, '15')], help_text='Please select a GS grade level.', unique_for_date='g_start_date'),
        ),
    ]