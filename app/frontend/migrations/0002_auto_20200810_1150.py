#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 10/08/2020 12:49.

# Generated by Django 3.0.2 on 2020-08-10 14:50

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('frontend', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Notifications',
            new_name='NotificationsMessages',
        ),
    ]