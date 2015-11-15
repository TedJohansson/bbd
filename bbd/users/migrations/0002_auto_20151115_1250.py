# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='logindetails',
            name='firstname',
            field=models.CharField(default=datetime.datetime(2015, 11, 15, 12, 50, 24, 594911, tzinfo=utc), max_length=60),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='logindetails',
            name='lastname',
            field=models.CharField(default=datetime.datetime(2015, 11, 15, 12, 50, 34, 339341, tzinfo=utc), max_length=60),
            preserve_default=False,
        ),
    ]
