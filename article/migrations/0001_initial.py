# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('article_first_name', models.CharField(max_length=20)),
                ('article_second_name', models.CharField(max_length=20)),
                ('article_third_name', models.CharField(max_length=20)),
                ('article_pasport_number', models.CharField(max_length=20)),
                ('article_birthdate', models.DateField()),
                ('article_sex', models.CharField(max_length=2)),
                ('article_other', models.TextField()),
            ],
            options={
                'db_table': 'article',
            },
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comments_pasport_number', models.CharField(max_length=20)),
                ('comments_takedate', models.DateField()),
                ('comments_other', models.TextField()),
                ('comments_article', models.ForeignKey(to='article.Article')),
            ],
            options={
                'db_table': 'comments',
            },
        ),
    ]
