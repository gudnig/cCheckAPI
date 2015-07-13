# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fighters', '0007_fighter_is_newbie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fighter',
            name='is_newbie',
            field=models.BooleanField(default=True),
        ),
    ]
