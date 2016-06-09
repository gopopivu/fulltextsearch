# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0002_auto_20160609_1048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='searchresult',
            name='filename',
            field=models.CharField(unique=True, max_length=255),
        ),
    ]
