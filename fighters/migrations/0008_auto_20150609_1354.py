# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fighters', '0007_auto_20150604_1539'),
    ]

    operations = [
        migrations.AlterField(
            model_name='practicesession',
            name='date',
            field=models.DateField(unique=True),
        ),
    ]
