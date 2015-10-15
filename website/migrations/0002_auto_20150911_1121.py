# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='thumbnail',
            field=models.ImageField(upload_to=b'gallery'),
        ),
    ]
