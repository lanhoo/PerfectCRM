# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MenuUrl',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('url_type', models.SmallIntegerField(default=1, choices=[(0, 'absolute'), (1, 'dynamic')])),
                ('url_name', models.CharField(max_length=64, unique=True)),
                ('url_detail', models.CharField(max_length=128)),
            ],
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='role',
            name='menu',
            field=models.ManyToManyField(to='crm.MenuUrl'),
        ),
    ]
