#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 18/07/2020 14:46.

# Generated by Django 3.0.2 on 2020-07-18 17:15

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('customer', '0002_auto_20200718_1415'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('config', '0002_auto_20200718_1415'),
        ('device', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicaldevice',
            name='created_by',
            field=models.ForeignKey(blank=True, db_constraint=False, help_text='Usuário que criou.', null=True,
                                    on_delete=django.db.models.deletion.DO_NOTHING, related_name='+',
                                    to=settings.AUTH_USER_MODEL, verbose_name='Criado por'),
        ),
        migrations.AddField(
            model_name='historicaldevice',
            name='customer',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True,
                                    on_delete=django.db.models.deletion.DO_NOTHING, related_name='+',
                                    to='customer.Customer', verbose_name='Cliente'),
        ),
        migrations.AddField(
            model_name='historicaldevice',
            name='history_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+',
                                    to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='historicaldevice',
            name='model',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True,
                                    on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='config.Model',
                                    verbose_name='Modelo'),
        ),
        migrations.AddField(
            model_name='historicaldevice',
            name='type',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True,
                                    on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='config.Type',
                                    verbose_name='Tipo'),
        ),
        migrations.AddField(
            model_name='device',
            name='brand',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='config.Brand',
                                    verbose_name='Marca'),
        ),
        migrations.AddField(
            model_name='device',
            name='capacity',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='config.Capacity',
                                    verbose_name='Capacidade'),
        ),
        migrations.AddField(
            model_name='device',
            name='created_by',
            field=models.ForeignKey(blank=True, help_text='Usuário que criou.', null=True,
                                    on_delete=django.db.models.deletion.SET_NULL, related_name='device_created_by',
                                    to=settings.AUTH_USER_MODEL, verbose_name='Criado por'),
        ),
        migrations.AddField(
            model_name='device',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.Customer',
                                    verbose_name='Cliente'),
        ),
        migrations.AddField(
            model_name='device',
            name='model',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='config.Model',
                                    verbose_name='Modelo'),
        ),
        migrations.AddField(
            model_name='device',
            name='type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='config.Type',
                                    verbose_name='Tipo'),
        ),
    ]
