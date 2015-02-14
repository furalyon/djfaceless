# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='playerClass',
            field=models.CharField(max_length=255, null=True, verbose_name='playerClass', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='mechanic',
            name='slug',
            field=models.SlugField(default='field-populated-by-system-when-saving', unique=True, max_length=255, verbose_name='Slug'),
            preserve_default=True,
        ),
    ]
