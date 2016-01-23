# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0005_reviewrequest_repo_avatar_url'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reviewrequest',
            old_name='repo_avatar_Url',
            new_name='repo_avatar_url',
        ),
    ]
