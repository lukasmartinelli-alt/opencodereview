# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviewrequest',
            name='status',
            field=models.IntegerField(default=0, choices=[(0, 'Pending'), (1, 'Reviewed')]),
        ),
    ]
