#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 22/07/2020 22:57.

# Generated by Django 3.0.2 on 2020-07-23 01:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ('config', '0003_city_historicalcity'),
        ('customer', '0004_auto_20200722_1752'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AddField(
            model_name='customer',
            name='phone_1',
            field=models.CharField(blank=True, max_length=15, verbose_name='telefone 1'),
        ),
        migrations.AddField(
            model_name='customer',
            name='phone_2',
            field=models.CharField(blank=True, max_length=15, verbose_name='telefone 2'),
        ),
        migrations.AddField(
            model_name='historicalcustomer',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AddField(
            model_name='historicalcustomer',
            name='phone_1',
            field=models.CharField(blank=True, max_length=15, verbose_name='telefone 1'),
        ),
        migrations.AddField(
            model_name='historicalcustomer',
            name='phone_2',
            field=models.CharField(blank=True, max_length=15, verbose_name='telefone 2'),
        ),
        migrations.AlterField(
            model_name='customeraddress',
            name='city',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL,
                                    to='config.City', verbose_name='Cidade'),
        ),
        migrations.AlterField(
            model_name='customeraddress',
            name='state',
            field=models.CharField(blank=True,
                                   choices=[('AC', 'ACRE'), ('AL', 'ALAGOAS'), ('AP', 'AMAPA'), ('AM', 'AMAZONAS'),
                                            ('BA', 'BAHIA'), ('CE', 'CEARA'), ('DF', 'DISTRITO_FEDERAL'),
                                            ('ES', 'ESPIRITO_SANTO'), ('GO', 'GOIAS'), ('MA', 'MARANHAO'),
                                            ('MT', 'MATO_GROSSO'), ('MS', 'MATO_GROSSO_DO_SUL'), ('MG', 'MINAS_GERAIS'),
                                            ('PA', 'PARA'), ('PB', 'PARAIBA'), ('PR', 'PARANA'), ('PE', 'PERNAMBUCO'),
                                            ('PI', 'PIAUI'), ('RJ', 'RIO_DE_JANEIRO'), ('RN', 'RIO_GRANDE_DO_NORTE'),
                                            ('RS', 'RIO_GRANDE_DO_SUL'), ('RO', 'RONDONIA'), ('RR', 'RORAIMA'),
                                            ('SC', 'SANTA_CATARINA'), ('SP', 'SAO_PAULO'), ('SE', 'SERGIPE'),
                                            ('TO', 'TOCANTINS')], max_length=2, verbose_name='Estado'),
        ),
        migrations.AlterField(
            model_name='historicalcustomeraddress',
            name='city',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True,
                                    on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='config.City',
                                    verbose_name='Cidade'),
        ),
        migrations.AlterField(
            model_name='historicalcustomeraddress',
            name='state',
            field=models.CharField(blank=True,
                                   choices=[('AC', 'ACRE'), ('AL', 'ALAGOAS'), ('AP', 'AMAPA'), ('AM', 'AMAZONAS'),
                                            ('BA', 'BAHIA'), ('CE', 'CEARA'), ('DF', 'DISTRITO_FEDERAL'),
                                            ('ES', 'ESPIRITO_SANTO'), ('GO', 'GOIAS'), ('MA', 'MARANHAO'),
                                            ('MT', 'MATO_GROSSO'), ('MS', 'MATO_GROSSO_DO_SUL'), ('MG', 'MINAS_GERAIS'),
                                            ('PA', 'PARA'), ('PB', 'PARAIBA'), ('PR', 'PARANA'), ('PE', 'PERNAMBUCO'),
                                            ('PI', 'PIAUI'), ('RJ', 'RIO_DE_JANEIRO'), ('RN', 'RIO_GRANDE_DO_NORTE'),
                                            ('RS', 'RIO_GRANDE_DO_SUL'), ('RO', 'RONDONIA'), ('RR', 'RORAIMA'),
                                            ('SC', 'SANTA_CATARINA'), ('SP', 'SAO_PAULO'), ('SE', 'SERGIPE'),
                                            ('TO', 'TOCANTINS')], max_length=2, verbose_name='Estado'),
        ),
    ]
