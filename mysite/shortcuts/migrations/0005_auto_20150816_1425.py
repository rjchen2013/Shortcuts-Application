# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shortcuts', '0004_auto_20150816_1410'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choices',
            name='first_key',
            field=models.CharField(choices=[('Ctrl', 'Ctrl'), ('Shift', 'Shift'), ('Alt', 'Alt')], max_length=10),
        ),
        migrations.AlterField(
            model_name='choices',
            name='second_key',
            field=models.CharField(choices=[('C', 'C'), ('V', 'V'), ('S', 'S'), ('A', 'A'), ('Delete', 'Delete'), ('Enter', 'Enter')], max_length=10),
        ),
    ]
