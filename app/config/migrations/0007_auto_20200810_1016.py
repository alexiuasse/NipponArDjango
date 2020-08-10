#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 10/08/2020 12:49.

# Generated by Django 3.0.2 on 2020-08-10 13:16

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('config', '0006_auto_20200805_1900'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historicalstatusservice',
            name='badge_class',
        ),
        migrations.RemoveField(
            model_name='statusservice',
            name='badge_class',
        ),
        migrations.AddField(
            model_name='historicalstatusservice',
            name='contextual',
            field=models.CharField(blank=True, choices=[('success', 'VERDE'), ('primary', 'AZUL'), ('info', 'CIANO'),
                                                        ('warning', 'AMARELO'), ('danger', 'VERMELHO'),
                                                        ('default', 'CINZA')], max_length=20, verbose_name='cor'),
        ),
        migrations.AddField(
            model_name='statusservice',
            name='contextual',
            field=models.CharField(blank=True, choices=[('success', 'VERDE'), ('primary', 'AZUL'), ('info', 'CIANO'),
                                                        ('warning', 'AMARELO'), ('danger', 'VERMELHO'),
                                                        ('default', 'CINZA')], max_length=20, verbose_name='cor'),
        ),
    ]