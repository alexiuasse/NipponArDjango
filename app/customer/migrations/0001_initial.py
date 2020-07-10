# Generated by Django 3.0.2 on 2020-07-10 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_by', models.CharField(blank=True, help_text='Usuário que criou.', max_length=50, verbose_name='criado por')),
                ('created_in', models.DateField(auto_now_add=True, help_text='Data em que foi criado.', verbose_name='criado em')),
                ('updated_in', models.DateField(auto_now=True, help_text='Data em que foi atualizado.', verbose_name='autalizado em')),
                ('updated_by', models.CharField(blank=True, help_text='Último usuário a editar.', max_length=50, verbose_name='modificado por')),
                ('name', models.CharField(max_length=128, verbose_name='nome')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
