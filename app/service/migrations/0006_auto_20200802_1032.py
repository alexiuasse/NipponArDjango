#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 02/08/2020 12:00.

# Generated by Django 3.0.2 on 2020-08-02 13:32

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('service', '0005_auto_20200802_1025'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historicalorderofservice',
            name='device',
        ),
        migrations.RemoveField(
            model_name='orderofservice',
            name='device',
        ),
    ]