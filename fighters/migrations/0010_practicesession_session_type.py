# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fighters', '0009_auto_20150609_1417'),
    ]

    operations = [
        migrations.AddField(
            model_name='practicesession',
            name='session_type',
            field=models.CharField(default='Bardagaæfing', max_length=20),
            preserve_default=False,
        ),
    ]
