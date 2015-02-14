# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0002_auto_20150214_1241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='collectible',
            field=models.BooleanField(default=False, verbose_name='collectible'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='card',
            name='elite',
            field=models.BooleanField(default=False, verbose_name='elite'),
            preserve_default=True,
        ),
    ]
