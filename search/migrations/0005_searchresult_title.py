# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0004_searchresult_normalized_html'),
    ]

    operations = [
        migrations.AddField(
            model_name='searchresult',
            name='title',
            field=models.CharField(default=b'', max_length=255),
        ),
    ]
