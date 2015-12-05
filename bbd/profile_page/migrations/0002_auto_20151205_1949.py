# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_page', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='accepted_eula',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='favorite_animal',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='favorite_movie',
            field=models.CharField(default=b'The one with the guy.', max_length=200),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='full_name',
            field=models.CharField(default=b'Anon', max_length=200),
        ),
    ]
