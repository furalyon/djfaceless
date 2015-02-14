# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.CharField(max_length=255, serialize=False, verbose_name='id', primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255, verbose_name='name')),
                ('cost', models.IntegerField(verbose_name='cost')),
                ('type', models.CharField(max_length=255, verbose_name='type')),
                ('rarity', models.CharField(max_length=255, verbose_name='rarity')),
                ('playerClass', models.CharField(max_length=255, verbose_name='playerClass')),
                ('attack', models.IntegerField(null=True, verbose_name='attack', blank=True)),
                ('health', models.IntegerField(null=True, verbose_name='health', blank=True)),
                ('durability', models.IntegerField(null=True, verbose_name='durability', blank=True)),
                ('text', models.CharField(max_length=255, null=True, verbose_name='text', blank=True)),
                ('race', models.CharField(max_length=255, null=True, verbose_name='race', blank=True)),
                ('collectible', models.BooleanField(default=True, verbose_name='collectible')),
                ('faction', models.CharField(max_length=255, null=True, verbose_name='faction', blank=True)),
                ('inPlayText', models.CharField(max_length=255, null=True, verbose_name='inPlayText', blank=True)),
                ('flavor', models.CharField(max_length=255, null=True, verbose_name='flavor', blank=True)),
                ('artist', models.CharField(max_length=255, null=True, verbose_name='artist', blank=True)),
                ('elite', models.BooleanField(default=True, verbose_name='elite')),
                ('howToGet', models.CharField(max_length=255, null=True, verbose_name='how to get', blank=True)),
                ('howToGetGold', models.CharField(max_length=255, null=True, verbose_name='how to get golden version', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Mechanic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255, verbose_name='name')),
                ('slug', models.SlugField(default='Field populated by system when saving', unique=True, max_length=255, verbose_name='Slug')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='card',
            name='mechanics',
            field=models.ManyToManyField(to='cards.Mechanic', null=True, verbose_name='mechanics'),
            preserve_default=True,
        ),
    ]
