#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 02/08/2020 12:00.

# Generated by Django 3.0.2 on 2020-08-02 14:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('service', '0006_auto_20200802_1032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalorderofservice',
            name='status',
            field=models.IntegerField(choices=[(0, 'NOVO'), (1, 'EM_ANDAMENTO'), (2, 'FINALIZADO')], default=0,
                                      verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='orderofservice',
            name='status',
            field=models.IntegerField(choices=[(0, 'NOVO'), (1, 'EM_ANDAMENTO'), (2, 'FINALIZADO')], default=0,
                                      verbose_name='Status'),
        ),
    ]