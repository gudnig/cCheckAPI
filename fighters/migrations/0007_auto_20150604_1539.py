# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fighters', '0006_auto_20150601_2236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='practicesession',
            name='description',
            field=models.CharField(blank=True, max_length=200, default=''),
            preserve_default=False,
        ),
    ]
