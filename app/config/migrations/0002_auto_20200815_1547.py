#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 15/08/2020 15:57.

# Generated by Django 3.0.2 on 2020-08-15 18:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('config', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='typeofservice',
            name='created_by',
            field=models.ForeignKey(blank=True, help_text='Usuário que criou.', null=True,
                                    on_delete=django.db.models.deletion.SET_NULL,
                                    related_name='typeofservice_created_by', to=settings.AUTH_USER_MODEL,
                                    verbose_name='Criado por'),
        ),
        migrations.AddField(
            model_name='type',
            name='created_by',
            field=models.ForeignKey(blank=True, help_text='Usuário que criou.', null=True,
                                    on_delete=django.db.models.deletion.SET_NULL, related_name='type_created_by',
                                    to=settings.AUTH_USER_MODEL, verbose_name='Criado por'),
        ),
        migrations.AddField(
            model_name='statusservice',
            name='created_by',
            field=models.ForeignKey(blank=True, help_text='Usuário que criou.', null=True,
                                    on_delete=django.db.models.deletion.SET_NULL,
                                    related_name='statusservice_created_by', to=settings.AUTH_USER_MODEL,
                                    verbose_name='Criado por'),
        ),
        migrations.AddField(
            model_name='model',
            name='created_by',
            field=models.ForeignKey(blank=True, help_text='Usuário que criou.', null=True,
                                    on_delete=django.db.models.deletion.SET_NULL, related_name='model_created_by',
                                    to=settings.AUTH_USER_MODEL, verbose_name='Criado por'),
        ),
        migrations.AddField(
            model_name='historicaltypeofservice',
            name='created_by',
            field=models.ForeignKey(blank=True, db_constraint=False, help_text='Usuário que criou.', null=True,
                                    on_delete=django.db.models.deletion.DO_NOTHING, related_name='+',
                                    to=settings.AUTH_USER_MODEL, verbose_name='Criado por'),
        ),
        migrations.AddField(
            model_name='historicaltypeofservice',
            name='history_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+',
                                    to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='historicaltype',
            name='created_by',
            field=models.ForeignKey(blank=True, db_constraint=False, help_text='Usuário que criou.', null=True,
                                    on_delete=django.db.models.deletion.DO_NOTHING, related_name='+',
                                    to=settings.AUTH_USER_MODEL, verbose_name='Criado por'),
        ),
        migrations.AddField(
            model_name='historicaltype',
            name='history_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+',
                                    to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='historicalstatusservice',
            name='created_by',
            field=models.ForeignKey(blank=True, db_constraint=False, help_text='Usuário que criou.', null=True,
                                    on_delete=django.db.models.deletion.DO_NOTHING, related_name='+',
                                    to=settings.AUTH_USER_MODEL, verbose_name='Criado por'),
        ),
        migrations.AddField(
            model_name='historicalstatusservice',
            name='history_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+',
                                    to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='historicalmodel',
            name='created_by',
            field=models.ForeignKey(blank=True, db_constraint=False, help_text='Usuário que criou.', null=True,
                                    on_delete=django.db.models.deletion.DO_NOTHING, related_name='+',
                                    to=settings.AUTH_USER_MODEL, verbose_name='Criado por'),
        ),
        migrations.AddField(
            model_name='historicalmodel',
            name='history_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+',
                                    to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='historicaldeviceparts',
            name='created_by',
            field=models.ForeignKey(blank=True, db_constraint=False, help_text='Usuário que criou.', null=True,
                                    on_delete=django.db.models.deletion.DO_NOTHING, related_name='+',
                                    to=settings.AUTH_USER_MODEL, verbose_name='Criado por'),
        ),
        migrations.AddField(
            model_name='historicaldeviceparts',
            name='history_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+',
                                    to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='historicalcity',
            name='created_by',
            field=models.ForeignKey(blank=True, db_constraint=False, help_text='Usuário que criou.', null=True,
                                    on_delete=django.db.models.deletion.DO_NOTHING, related_name='+',
                                    to=settings.AUTH_USER_MODEL, verbose_name='Criado por'),
        ),
        migrations.AddField(
            model_name='historicalcity',
            name='history_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+',
                                    to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='historicalcapacity',
            name='created_by',
            field=models.ForeignKey(blank=True, db_constraint=False, help_text='Usuário que criou.', null=True,
                                    on_delete=django.db.models.deletion.DO_NOTHING, related_name='+',
                                    to=settings.AUTH_USER_MODEL, verbose_name='Criado por'),
        ),
        migrations.AddField(
            model_name='historicalcapacity',
            name='history_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+',
                                    to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='historicalbrand',
            name='created_by',
            field=models.ForeignKey(blank=True, db_constraint=False, help_text='Usuário que criou.', null=True,
                                    on_delete=django.db.models.deletion.DO_NOTHING, related_name='+',
                                    to=settings.AUTH_USER_MODEL, verbose_name='Criado por'),
        ),
        migrations.AddField(
            model_name='historicalbrand',
            name='history_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+',
                                    to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='deviceparts',
            name='created_by',
            field=models.ForeignKey(blank=True, help_text='Usuário que criou.', null=True,
                                    on_delete=django.db.models.deletion.SET_NULL, related_name='deviceparts_created_by',
                                    to=settings.AUTH_USER_MODEL, verbose_name='Criado por'),
        ),
        migrations.AddField(
            model_name='city',
            name='created_by',
            field=models.ForeignKey(blank=True, help_text='Usuário que criou.', null=True,
                                    on_delete=django.db.models.deletion.SET_NULL, related_name='city_created_by',
                                    to=settings.AUTH_USER_MODEL, verbose_name='Criado por'),
        ),
        migrations.AddField(
            model_name='capacity',
            name='created_by',
            field=models.ForeignKey(blank=True, help_text='Usuário que criou.', null=True,
                                    on_delete=django.db.models.deletion.SET_NULL, related_name='capacity_created_by',
                                    to=settings.AUTH_USER_MODEL, verbose_name='Criado por'),
        ),
        migrations.AddField(
            model_name='brand',
            name='created_by',
            field=models.ForeignKey(blank=True, help_text='Usuário que criou.', null=True,
                                    on_delete=django.db.models.deletion.SET_NULL, related_name='brand_created_by',
                                    to=settings.AUTH_USER_MODEL, verbose_name='Criado por'),
        ),
    ]