# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0002_auto_20180622_0956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='role',
            name='menu',
            field=models.ManyToManyField(blank=True, to='crm.MenuUrl'),
        ),
    ]
