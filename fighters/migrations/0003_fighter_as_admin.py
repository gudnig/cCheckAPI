# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fighters', '0002_fighter_practicesession'),
    ]

    operations = [
        migrations.AddField(
            model_name='fighter',
            name='as_admin',
            field=models.BooleanField(default=False),
        ),
    ]
