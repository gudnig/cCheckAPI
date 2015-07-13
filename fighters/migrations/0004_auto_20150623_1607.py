# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fighters', '0003_fighter_as_admin'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fighter',
            name='user',
        ),
        migrations.RemoveField(
            model_name='practicesession',
            name='full_attendance',
        ),
        migrations.RemoveField(
            model_name='practicesession',
            name='half_attendance',
        ),
        migrations.DeleteModel(
            name='Fighter',
        ),
        migrations.DeleteModel(
            name='PracticeSession',
        ),
    ]
