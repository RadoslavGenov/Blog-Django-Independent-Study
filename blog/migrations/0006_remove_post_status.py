# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20170222_1230'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='status',
        ),
    ]
