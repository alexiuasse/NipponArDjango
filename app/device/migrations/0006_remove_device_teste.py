#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 17/07/2020 23:30.

# Generated by Django 3.0.2 on 2020-07-18 01:32

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('device', '0005_device_teste'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='device',
            name='teste',
        ),
    ]