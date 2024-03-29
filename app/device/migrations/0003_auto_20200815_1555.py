#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 15/08/2020 15:57.

# Generated by Django 3.0.2 on 2020-08-15 18:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ('config', '0002_auto_20200815_1547'),
        ('device', '0002_auto_20200815_1547'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='brand',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL,
                                    to='config.Brand', verbose_name='Marca'),
        ),
        migrations.AlterField(
            model_name='device',
            name='capacity',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL,
                                    to='config.Capacity', verbose_name='Capacidade'),
        ),
        migrations.AlterField(
            model_name='device',
            name='model',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL,
                                    to='config.Model', verbose_name='Modelo'),
        ),
        migrations.AlterField(
            model_name='device',
            name='type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL,
                                    to='config.Type', verbose_name='Tipo'),
        ),
    ]
