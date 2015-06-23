# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fighters', '0005_auto_20150522_1051'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='practicesession',
            name='attendance',
        ),
        migrations.AddField(
            model_name='practicesession',
            name='full_attendance',
            field=models.ManyToManyField(related_name='full_attendance', to='fighters.Fighter'),
        ),
        migrations.AddField(
            model_name='practicesession',
            name='half_attendance',
            field=models.ManyToManyField(related_name='half_attendance', to='fighters.Fighter'),
        ),
    ]
