# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fighters', '0010_practicesession_session_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='fighter',
            name='can_post_notifications',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='fighter',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='fighter',
            name='is_trainer',
            field=models.BooleanField(default=False),
        ),
    ]
