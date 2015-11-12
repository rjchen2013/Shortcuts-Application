# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shortcuts', '0002_auto_20150815_1411'),
    ]

    operations = [
        migrations.CreateModel(
            name='Choices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('first_key', models.CharField(choices=[('Ctrl', 'Ctrl'), ('Shift', 'Shift'), ('Alt', 'Alt')], max_length=5)),
                ('second_key', models.CharField(choices=[('C', 'C'), ('V', 'V'), ('S', 'S'), ('A', 'A')], max_length=5)),
            ],
        ),
    ]
