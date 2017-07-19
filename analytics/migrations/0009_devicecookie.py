"""
Copyright (C) 2017 Semester.ly Technologies, LLC

Semester.ly is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Semester.ly is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
"""

# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-01-14 23:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0015_merge'),
        ('analytics', '0008_analyticscoursesearch_courses'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeviceCookie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_online', models.DateTimeField(auto_now_add=True)),
                ('student', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='student.Student')),
            ],
        ),
    ]
