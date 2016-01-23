# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_auto_20160123_1830'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reviewrequest',
            name='create_issue',
        ),
    ]
