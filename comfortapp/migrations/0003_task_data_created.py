# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('comfortapp', '0002_task'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='data_created',
            field=models.DateTimeField(default=datetime.datetime(2016, 5, 5, 18, 9, 35, 93525, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
