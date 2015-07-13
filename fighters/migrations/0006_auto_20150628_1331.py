# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fighters', '0005_fighter_practicesession'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fighter',
            name='status',
        ),
        migrations.AddField(
            model_name='fighter',
            name='is_archer',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='fighter',
            name='is_fighter',
            field=models.BooleanField(default=False),
        ),
    ]
