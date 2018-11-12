# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('performance', '0006_auto_20161015_1145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assessmentlinedetail',
            name='description',
            field=models.TextField(verbose_name='得分标准', default=''),
        ),
    ]
