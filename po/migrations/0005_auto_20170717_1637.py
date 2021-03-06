# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-17 20:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('po', '0004_auto_20170717_1329'),
    ]

    operations = [
        migrations.AddField(
            model_name='cost_center',
            name='dept_code',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='cost_center',
            name='name',
            field=models.CharField(max_length=140),
        ),
        migrations.AlterField(
            model_name='po',
            name='tax_amt',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=19, null=True),
        ),
    ]
