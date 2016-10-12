# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-12 18:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Target',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('target_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='TargetWiki',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wiki_name', models.CharField(max_length=200)),
                ('wiki_hits', models.IntegerField(default=0)),
                ('target', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='search.Target')),
            ],
        ),
    ]