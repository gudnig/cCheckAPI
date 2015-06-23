# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fighters', '0003_practicesession'),
    ]

    operations = [
        migrations.AlterField(
            model_name='practicesession',
            name='attendance',
            field=models.ManyToManyField(null=True, to='fighters.Fighter', related_name='attendance'),
        ),
        migrations.AlterField(
            model_name='practicesession',
            name='description',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
