# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0004_remove_reviewrequest_create_issue'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviewrequest',
            name='repo_avatar_Url',
            field=models.URLField(default='https://avatars.githubusercontent.com/u/1288339?v=3'),
            preserve_default=False,
        ),
    ]
