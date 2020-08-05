#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 05/08/2020 19:01.

# Generated by Django 3.0.2 on 2020-08-05 22:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('service', '0008_auto_20200802_1707'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalorderofservice',
            name='scheduled',
            field=models.BooleanField(default=False, verbose_name='agendado'),
        ),
        migrations.AddField(
            model_name='orderofservice',
            name='scheduled',
            field=models.BooleanField(default=False, verbose_name='agendado'),
        ),
    ]
