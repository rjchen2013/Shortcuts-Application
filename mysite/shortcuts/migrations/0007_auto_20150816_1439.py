# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shortcuts', '0006_auto_20150816_1437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choices',
            name='name',
            field=models.CharField(max_length=60),
        ),
    ]
