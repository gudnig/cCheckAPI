# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fighters', '0004_auto_20150522_0954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='practicesession',
            name='attendance',
            field=models.ManyToManyField(related_name='attendance', to='fighters.Fighter'),
        ),
    ]
