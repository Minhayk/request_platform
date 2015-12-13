# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='request_status',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('status', models.TextField(default='Ընթացիկ')),
            ],
        ),
    ]
