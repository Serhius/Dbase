# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DBase',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.CharField(max_length=20)),
                ('oper', models.CharField(max_length=4)),
                ('date', models.DateField(blank=True)),
                ('time', models.TimeField()),
                ('stat', models.CharField(max_length=5)),
                ('reason', models.CharField(max_length=5)),
            ],
            options={
                'db_table': 'dbase',
            },
        ),
    ]
