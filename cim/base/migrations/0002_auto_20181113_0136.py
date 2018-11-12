# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='mobile',
            field=models.CharField(verbose_name='电话', max_length=20, unique=True, blank=True, null=True, default=''),
        ),
        migrations.AlterField(
            model_name='user',
            name='short_phone',
            field=models.CharField(verbose_name='短号', max_length=10, blank=True, null=True, default=''),
        ),
        migrations.AlterField(
            model_name='user',
            name='username_zh',
            field=models.CharField(verbose_name='中文名称', max_length=20, blank=True, null=True, default=''),
        ),
    ]
