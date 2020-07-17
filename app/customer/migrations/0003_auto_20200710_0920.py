#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 17/07/2020 11:56.

# Generated by Django 3.0.2 on 2020-07-10 12:20

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('customer', '0002_auto_20200710_0914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='created_by',
            field=models.ForeignKey(blank=True, help_text='Usuário que criou.', null=True,
                                    on_delete=django.db.models.deletion.SET_NULL, related_name='customer_created_by',
                                    to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='customer',
            name='updated_by',
            field=models.ForeignKey(blank=True, help_text='Usuário que modificou.', null=True,
                                    on_delete=django.db.models.deletion.SET_NULL, related_name='customer_updated_by',
                                    to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='customer',
            name='updated_in',
            field=models.DateField(auto_now=True, help_text='Data em que foi atualizado.',
                                   verbose_name='atualizado em'),
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_in',
                 models.DateField(auto_now_add=True, help_text='Data em que foi criado.', verbose_name='criado em')),
                ('updated_in', models.DateField(auto_now=True, help_text='Data em que foi atualizado.',
                                                verbose_name='atualizado em')),
                ('created_by', models.ForeignKey(blank=True, help_text='Usuário que criou.', null=True,
                                                 on_delete=django.db.models.deletion.SET_NULL,
                                                 related_name='address_created_by', to=settings.AUTH_USER_MODEL)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.Customer',
                                               verbose_name='Cliente')),
                ('updated_by', models.ForeignKey(blank=True, help_text='Usuário que modificou.', null=True,
                                                 on_delete=django.db.models.deletion.SET_NULL,
                                                 related_name='address_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]