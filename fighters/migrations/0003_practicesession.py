# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fighters', '0002_auto_20150522_0028'),
    ]

    operations = [
        migrations.CreateModel(
            name='PracticeSession',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=200)),
                ('date', models.DateField()),
                ('attendance', models.ManyToManyField(to='fighters.Fighter')),
            ],
        ),
    ]
