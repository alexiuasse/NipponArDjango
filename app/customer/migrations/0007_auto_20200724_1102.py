#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 24/07/2020 18:57.

# Generated by Django 3.0.2 on 2020-07-24 14:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ('customer', '0006_auto_20200724_1051'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='address',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL,
                                    related_name='address_teste', to='customer.CustomerAddress',
                                    verbose_name='Endereço'),
        ),
        migrations.AddField(
            model_name='historicalcustomer',
            name='address',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True,
                                    on_delete=django.db.models.deletion.DO_NOTHING, related_name='+',
                                    to='customer.CustomerAddress', verbose_name='Endereço'),
        ),
    ]
