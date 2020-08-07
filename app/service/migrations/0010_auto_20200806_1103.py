#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 07/08/2020 15:06.

# Generated by Django 3.0.2 on 2020-08-06 14:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('config', '0006_auto_20200805_1900'),
        ('service', '0009_auto_20200805_1900'),
    ]

    operations = [
        migrations.CreateModel(
            name='PartsExchanged',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_in',
                 models.DateField(auto_now_add=True, help_text='Data em que foi criado.', verbose_name='criado em')),
                ('quantity', models.IntegerField(default=1)),
                ('created_by', models.ForeignKey(blank=True, help_text='Usuário que criou.', null=True,
                                                 on_delete=django.db.models.deletion.SET_NULL,
                                                 related_name='partsexchanged_created_by', to=settings.AUTH_USER_MODEL,
                                                 verbose_name='Criado por')),
                ('part', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='config.DeviceParts',
                                           verbose_name='Peça')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='HistoricalPartsExchanged',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('created_in', models.DateField(blank=True, editable=False, help_text='Data em que foi criado.',
                                                verbose_name='criado em')),
                ('quantity', models.IntegerField(default=1)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type',
                 models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('created_by',
                 models.ForeignKey(blank=True, db_constraint=False, help_text='Usuário que criou.', null=True,
                                   on_delete=django.db.models.deletion.DO_NOTHING, related_name='+',
                                   to=settings.AUTH_USER_MODEL, verbose_name='Criado por')),
                ('history_user',
                 models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+',
                                   to=settings.AUTH_USER_MODEL)),
                ('part', models.ForeignKey(blank=True, db_constraint=False, null=True,
                                           on_delete=django.db.models.deletion.DO_NOTHING, related_name='+',
                                           to='config.DeviceParts', verbose_name='Peça')),
            ],
            options={
                'verbose_name': 'historical parts exchanged',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.AlterField(
            model_name='orderofservice',
            name='parts',
            field=models.ManyToManyField(blank=True, to='service.PartsExchanged', verbose_name='Peças'),
        ),
    ]
