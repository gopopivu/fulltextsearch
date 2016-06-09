# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0003_auto_20160609_1149'),
    ]

    operations = [
        migrations.AddField(
            model_name='searchresult',
            name='normalized_html',
            field=models.TextField(default=b''),
        ),
    ]
