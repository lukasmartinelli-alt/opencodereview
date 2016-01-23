# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.postgres.fields


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_reviewrequest_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reviewrequest',
            old_name='info',
            new_name='review_info',
        ),
        migrations.RemoveField(
            model_name='reviewrequest',
            name='github_repo',
        ),
        migrations.AddField(
            model_name='reviewrequest',
            name='repo_description',
            field=models.TextField(default='desc'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reviewrequest',
            name='repo_name',
            field=models.TextField(default='name'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reviewrequest',
            name='repo_owner',
            field=models.TextField(default='owner'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reviewrequest',
            name='repo_stars',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='reviewrequest',
            name='tags',
            field=django.contrib.postgres.fields.ArrayField(default=[], size=None, base_field=models.CharField(max_length=200), blank=True),
            preserve_default=False,
        ),
    ]
