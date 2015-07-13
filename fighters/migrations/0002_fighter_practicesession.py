# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('fighters', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fighter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=20)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('is_trainer', models.BooleanField(default=False)),
                ('can_post_notifications', models.BooleanField(default=False)),
                ('is_admin', models.BooleanField(default=False)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PracticeSession',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=200, blank=True)),
                ('date', models.DateField()),
                ('session_type', models.CharField(max_length=20)),
                ('full_attendance', models.ManyToManyField(to='fighters.Fighter', related_name='full_attendance')),
                ('half_attendance', models.ManyToManyField(to='fighters.Fighter', related_name='half_attendance')),
            ],
        ),
    ]
