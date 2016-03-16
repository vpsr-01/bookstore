# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=120)),
                ('author', models.CharField(max_length=120)),
                ('description', models.TextField()),
                ('publish_date', models.DateField(default=django.utils.timezone.now)),
                ('price', models.DecimalField(max_digits=8, decimal_places=2)),
                ('stock', models.IntegerField(default=0)),
            ],
        ),
    ]
