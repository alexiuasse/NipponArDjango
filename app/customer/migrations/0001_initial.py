#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 10/08/2020 13:23.

# Generated by Django 3.0.2 on 2020-08-10 16:21

from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('config', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalIndividualCustomer',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('created_in', models.DateField(blank=True, editable=False, help_text='Data em que foi criado.',
                                                verbose_name='criado em')),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('phone_1', models.CharField(blank=True, max_length=15, verbose_name='telefone')),
                ('phone_2', models.CharField(blank=True, max_length=15, verbose_name='celular')),
                ('street', models.CharField(blank=True, max_length=128, verbose_name='Rua')),
                ('number', models.CharField(blank=True, max_length=10, verbose_name='Número')),
                ('neighborhood', models.CharField(blank=True, max_length=128, verbose_name='Bairro')),
                ('apartment', models.CharField(blank=True, max_length=10, verbose_name='Apartamento')),
                ('block', models.CharField(blank=True, max_length=128, verbose_name='Bloco')),
                ('state', models.CharField(blank=True, choices=[('AC', 'ACRE'), ('AL', 'ALAGOAS'), ('AP', 'AMAPA'),
                                                                ('AM', 'AMAZONAS'), ('BA', 'BAHIA'), ('CE', 'CEARA'),
                                                                ('DF', 'DISTRITO_FEDERAL'), ('ES', 'ESPIRITO_SANTO'),
                                                                ('GO', 'GOIAS'), ('MA', 'MARANHAO'),
                                                                ('MT', 'MATO_GROSSO'), ('MS', 'MATO_GROSSO_DO_SUL'),
                                                                ('MG', 'MINAS_GERAIS'), ('PA', 'PARA'),
                                                                ('PB', 'PARAIBA'), ('PR', 'PARANA'),
                                                                ('PE', 'PERNAMBUCO'), ('PI', 'PIAUI'),
                                                                ('RJ', 'RIO_DE_JANEIRO'), ('RN', 'RIO_GRANDE_DO_NORTE'),
                                                                ('RS', 'RIO_GRANDE_DO_SUL'), ('RO', 'RONDONIA'),
                                                                ('RR', 'RORAIMA'), ('SC', 'SANTA_CATARINA'),
                                                                ('SP', 'SAO_PAULO'), ('SE', 'SERGIPE'),
                                                                ('TO', 'TOCANTINS')], max_length=2,
                                           verbose_name='Estado')),
                ('cep', models.CharField(blank=True, max_length=9, verbose_name='CEP')),
                ('address_line', models.CharField(blank=True, max_length=256, verbose_name='Endereço')),
                ('name', models.CharField(max_length=128, verbose_name='nome')),
                ('cpf', models.CharField(blank=True, max_length=14, verbose_name='CPF')),
                ('type', models.IntegerField(default=0)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type',
                 models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
            ],
            options={
                'verbose_name': 'historical individual customer',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalJuridicalCustomer',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('created_in', models.DateField(blank=True, editable=False, help_text='Data em que foi criado.',
                                                verbose_name='criado em')),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('phone_1', models.CharField(blank=True, max_length=15, verbose_name='telefone')),
                ('phone_2', models.CharField(blank=True, max_length=15, verbose_name='celular')),
                ('street', models.CharField(blank=True, max_length=128, verbose_name='Rua')),
                ('number', models.CharField(blank=True, max_length=10, verbose_name='Número')),
                ('neighborhood', models.CharField(blank=True, max_length=128, verbose_name='Bairro')),
                ('apartment', models.CharField(blank=True, max_length=10, verbose_name='Apartamento')),
                ('block', models.CharField(blank=True, max_length=128, verbose_name='Bloco')),
                ('state', models.CharField(blank=True, choices=[('AC', 'ACRE'), ('AL', 'ALAGOAS'), ('AP', 'AMAPA'),
                                                                ('AM', 'AMAZONAS'), ('BA', 'BAHIA'), ('CE', 'CEARA'),
                                                                ('DF', 'DISTRITO_FEDERAL'), ('ES', 'ESPIRITO_SANTO'),
                                                                ('GO', 'GOIAS'), ('MA', 'MARANHAO'),
                                                                ('MT', 'MATO_GROSSO'), ('MS', 'MATO_GROSSO_DO_SUL'),
                                                                ('MG', 'MINAS_GERAIS'), ('PA', 'PARA'),
                                                                ('PB', 'PARAIBA'), ('PR', 'PARANA'),
                                                                ('PE', 'PERNAMBUCO'), ('PI', 'PIAUI'),
                                                                ('RJ', 'RIO_DE_JANEIRO'), ('RN', 'RIO_GRANDE_DO_NORTE'),
                                                                ('RS', 'RIO_GRANDE_DO_SUL'), ('RO', 'RONDONIA'),
                                                                ('RR', 'RORAIMA'), ('SC', 'SANTA_CATARINA'),
                                                                ('SP', 'SAO_PAULO'), ('SE', 'SERGIPE'),
                                                                ('TO', 'TOCANTINS')], max_length=2,
                                           verbose_name='Estado')),
                ('cep', models.CharField(blank=True, max_length=9, verbose_name='CEP')),
                ('address_line', models.CharField(blank=True, max_length=256, verbose_name='Endereço')),
                ('name', models.CharField(max_length=128, verbose_name='razão Social')),
                ('cnpj', models.CharField(blank=True, max_length=18, verbose_name='CNPJ')),
                ('type', models.IntegerField(default=1)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type',
                 models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
            ],
            options={
                'verbose_name': 'historical juridical customer',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='IndividualCustomer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_in',
                 models.DateField(auto_now_add=True, help_text='Data em que foi criado.', verbose_name='criado em')),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('phone_1', models.CharField(blank=True, max_length=15, verbose_name='telefone')),
                ('phone_2', models.CharField(blank=True, max_length=15, verbose_name='celular')),
                ('street', models.CharField(blank=True, max_length=128, verbose_name='Rua')),
                ('number', models.CharField(blank=True, max_length=10, verbose_name='Número')),
                ('neighborhood', models.CharField(blank=True, max_length=128, verbose_name='Bairro')),
                ('apartment', models.CharField(blank=True, max_length=10, verbose_name='Apartamento')),
                ('block', models.CharField(blank=True, max_length=128, verbose_name='Bloco')),
                ('state', models.CharField(blank=True, choices=[('AC', 'ACRE'), ('AL', 'ALAGOAS'), ('AP', 'AMAPA'),
                                                                ('AM', 'AMAZONAS'), ('BA', 'BAHIA'), ('CE', 'CEARA'),
                                                                ('DF', 'DISTRITO_FEDERAL'), ('ES', 'ESPIRITO_SANTO'),
                                                                ('GO', 'GOIAS'), ('MA', 'MARANHAO'),
                                                                ('MT', 'MATO_GROSSO'), ('MS', 'MATO_GROSSO_DO_SUL'),
                                                                ('MG', 'MINAS_GERAIS'), ('PA', 'PARA'),
                                                                ('PB', 'PARAIBA'), ('PR', 'PARANA'),
                                                                ('PE', 'PERNAMBUCO'), ('PI', 'PIAUI'),
                                                                ('RJ', 'RIO_DE_JANEIRO'), ('RN', 'RIO_GRANDE_DO_NORTE'),
                                                                ('RS', 'RIO_GRANDE_DO_SUL'), ('RO', 'RONDONIA'),
                                                                ('RR', 'RORAIMA'), ('SC', 'SANTA_CATARINA'),
                                                                ('SP', 'SAO_PAULO'), ('SE', 'SERGIPE'),
                                                                ('TO', 'TOCANTINS')], max_length=2,
                                           verbose_name='Estado')),
                ('cep', models.CharField(blank=True, max_length=9, verbose_name='CEP')),
                ('address_line', models.CharField(blank=True, max_length=256, verbose_name='Endereço')),
                ('name', models.CharField(max_length=128, verbose_name='nome')),
                ('cpf', models.CharField(blank=True, max_length=14, verbose_name='CPF')),
                ('type', models.IntegerField(default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='JuridicalCustomer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_in',
                 models.DateField(auto_now_add=True, help_text='Data em que foi criado.', verbose_name='criado em')),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('phone_1', models.CharField(blank=True, max_length=15, verbose_name='telefone')),
                ('phone_2', models.CharField(blank=True, max_length=15, verbose_name='celular')),
                ('street', models.CharField(blank=True, max_length=128, verbose_name='Rua')),
                ('number', models.CharField(blank=True, max_length=10, verbose_name='Número')),
                ('neighborhood', models.CharField(blank=True, max_length=128, verbose_name='Bairro')),
                ('apartment', models.CharField(blank=True, max_length=10, verbose_name='Apartamento')),
                ('block', models.CharField(blank=True, max_length=128, verbose_name='Bloco')),
                ('state', models.CharField(blank=True, choices=[('AC', 'ACRE'), ('AL', 'ALAGOAS'), ('AP', 'AMAPA'),
                                                                ('AM', 'AMAZONAS'), ('BA', 'BAHIA'), ('CE', 'CEARA'),
                                                                ('DF', 'DISTRITO_FEDERAL'), ('ES', 'ESPIRITO_SANTO'),
                                                                ('GO', 'GOIAS'), ('MA', 'MARANHAO'),
                                                                ('MT', 'MATO_GROSSO'), ('MS', 'MATO_GROSSO_DO_SUL'),
                                                                ('MG', 'MINAS_GERAIS'), ('PA', 'PARA'),
                                                                ('PB', 'PARAIBA'), ('PR', 'PARANA'),
                                                                ('PE', 'PERNAMBUCO'), ('PI', 'PIAUI'),
                                                                ('RJ', 'RIO_DE_JANEIRO'), ('RN', 'RIO_GRANDE_DO_NORTE'),
                                                                ('RS', 'RIO_GRANDE_DO_SUL'), ('RO', 'RONDONIA'),
                                                                ('RR', 'RORAIMA'), ('SC', 'SANTA_CATARINA'),
                                                                ('SP', 'SAO_PAULO'), ('SE', 'SERGIPE'),
                                                                ('TO', 'TOCANTINS')], max_length=2,
                                           verbose_name='Estado')),
                ('cep', models.CharField(blank=True, max_length=9, verbose_name='CEP')),
                ('address_line', models.CharField(blank=True, max_length=256, verbose_name='Endereço')),
                ('name', models.CharField(max_length=128, verbose_name='razão Social')),
                ('cnpj', models.CharField(blank=True, max_length=18, verbose_name='CNPJ')),
                ('type', models.IntegerField(default=1)),
                ('city', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL,
                                           to='config.City', verbose_name='Cidade')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
