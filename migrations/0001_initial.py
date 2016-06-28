# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FeedMe',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('creation', models.DateField(auto_now=True)),
                ('pub_date', models.DateTimeField(auto_now=True, null=True)),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('url', models.CharField(max_length=140)),
            ],
            options={
                'ordering': ('-pub_date',),
            },
        ),
        migrations.CreateModel(
            name='SearchEngine',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('url', models.URLField()),
                ('ping_count', models.IntegerField(default=0)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
    ]
