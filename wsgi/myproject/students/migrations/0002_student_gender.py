# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='gender',
            field=models.CharField(default=datetime.datetime(2015, 9, 30, 18, 23, 35, 548680, tzinfo=utc), max_length=10),
            preserve_default=False,
        ),
    ]
