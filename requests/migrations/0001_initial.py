# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('divisions', '0001_initial'),
        ('request_types', '0001_initial'),
        ('request_status', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lists',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('purchase_purpose', models.CharField(max_length=150)),
                ('product_name', models.CharField(max_length=75)),
                ('product_price', models.FloatField(default=1)),
                ('product_quantity', models.FloatField(default=1)),
                ('comment', models.CharField(max_length=200)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('approved_date_head', models.DateTimeField(null=True, blank=True)),
                ('approved_date_admin', models.DateTimeField(null=True, blank=True)),
                ('approved_date_fin', models.DateTimeField(null=True, blank=True)),
                ('approved_date_CEO_DCEO', models.DateTimeField(null=True, blank=True)),
                ('Division', models.ForeignKey(to='divisions.divisions', related_name='divisions')),
                ('Initiator', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('request_type_id', models.ForeignKey(to='request_types.request_types', related_name='request_types')),
                ('status_id', models.ForeignKey(to='request_status.request_status', related_name='request_status')),
            ],
        ),
    ]
