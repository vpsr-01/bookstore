# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store', '0002_auto_20160317_1259'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookOrder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quantity', models.IntegerField(null=True)),
                ('payment_type', models.CharField(max_length=100, null=True)),
                ('payment_id', models.CharField(max_length=100, null=True)),
                ('book', models.ForeignKey(to='store.Book')),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('active', models.BooleanField(default=True)),
                ('order_date', models.DateField(null=True)),
                ('payment_type', models.CharField(max_length=100, null=True)),
                ('payment_id', models.CharField(max_length=100, null=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='bookorder',
            name='cart',
            field=models.ForeignKey(to='store.Cart'),
        ),
    ]
