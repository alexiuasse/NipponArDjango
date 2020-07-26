#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 25/07/2020 23:18.

# Generated by Django 3.0.2 on 2020-07-25 23:49

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('customer', '0014_auto_20200725_2042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='type',
            field=models.CharField(choices=[('PF', 'FISICA'), ('PJ', 'JURIDICA')], max_length=2, verbose_name='tipo'),
        ),
        migrations.AlterField(
            model_name='historicalcustomer',
            name='type',
            field=models.CharField(choices=[('PF', 'FISICA'), ('PJ', 'JURIDICA')], max_length=2, verbose_name='tipo'),
        ),
    ]
