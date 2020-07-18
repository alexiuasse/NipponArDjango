#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 17/07/2020 23:30.

# Generated by Django 3.0.2 on 2020-07-17 23:33

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('config', '0003_auto_20200717_1923'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='brand',
            name='quantity',
        ),
        migrations.RemoveField(
            model_name='capacity',
            name='quantity',
        ),
        migrations.RemoveField(
            model_name='model',
            name='quantity',
        ),
        migrations.RemoveField(
            model_name='type',
            name='quantity',
        ),
        migrations.RemoveField(
            model_name='unit',
            name='quantity',
        ),
        migrations.AlterField(
            model_name='brand',
            name='created_by',
            field=models.ForeignKey(blank=True, help_text='Usuário que criou.', null=True,
                                    on_delete=django.db.models.deletion.SET_NULL, related_name='brand_created_by',
                                    to=settings.AUTH_USER_MODEL, verbose_name='Criado por'),
        ),
        migrations.AlterField(
            model_name='brand',
            name='updated_by',
            field=models.ForeignKey(blank=True, help_text='Usuário que modificou.', null=True,
                                    on_delete=django.db.models.deletion.SET_NULL, related_name='brand_updated_by',
                                    to=settings.AUTH_USER_MODEL, verbose_name='Atualizado por'),
        ),
        migrations.AlterField(
            model_name='capacity',
            name='created_by',
            field=models.ForeignKey(blank=True, help_text='Usuário que criou.', null=True,
                                    on_delete=django.db.models.deletion.SET_NULL, related_name='capacity_created_by',
                                    to=settings.AUTH_USER_MODEL, verbose_name='Criado por'),
        ),
        migrations.AlterField(
            model_name='capacity',
            name='updated_by',
            field=models.ForeignKey(blank=True, help_text='Usuário que modificou.', null=True,
                                    on_delete=django.db.models.deletion.SET_NULL, related_name='capacity_updated_by',
                                    to=settings.AUTH_USER_MODEL, verbose_name='Atualizado por'),
        ),
        migrations.AlterField(
            model_name='model',
            name='created_by',
            field=models.ForeignKey(blank=True, help_text='Usuário que criou.', null=True,
                                    on_delete=django.db.models.deletion.SET_NULL, related_name='model_created_by',
                                    to=settings.AUTH_USER_MODEL, verbose_name='Criado por'),
        ),
        migrations.AlterField(
            model_name='model',
            name='updated_by',
            field=models.ForeignKey(blank=True, help_text='Usuário que modificou.', null=True,
                                    on_delete=django.db.models.deletion.SET_NULL, related_name='model_updated_by',
                                    to=settings.AUTH_USER_MODEL, verbose_name='Atualizado por'),
        ),
        migrations.AlterField(
            model_name='type',
            name='created_by',
            field=models.ForeignKey(blank=True, help_text='Usuário que criou.', null=True,
                                    on_delete=django.db.models.deletion.SET_NULL, related_name='type_created_by',
                                    to=settings.AUTH_USER_MODEL, verbose_name='Criado por'),
        ),
        migrations.AlterField(
            model_name='type',
            name='updated_by',
            field=models.ForeignKey(blank=True, help_text='Usuário que modificou.', null=True,
                                    on_delete=django.db.models.deletion.SET_NULL, related_name='type_updated_by',
                                    to=settings.AUTH_USER_MODEL, verbose_name='Atualizado por'),
        ),
        migrations.AlterField(
            model_name='unit',
            name='created_by',
            field=models.ForeignKey(blank=True, help_text='Usuário que criou.', null=True,
                                    on_delete=django.db.models.deletion.SET_NULL, related_name='unit_created_by',
                                    to=settings.AUTH_USER_MODEL, verbose_name='Criado por'),
        ),
        migrations.AlterField(
            model_name='unit',
            name='updated_by',
            field=models.ForeignKey(blank=True, help_text='Usuário que modificou.', null=True,
                                    on_delete=django.db.models.deletion.SET_NULL, related_name='unit_updated_by',
                                    to=settings.AUTH_USER_MODEL, verbose_name='Atualizado por'),
        ),
    ]
