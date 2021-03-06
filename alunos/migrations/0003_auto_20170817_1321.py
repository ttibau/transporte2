# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-17 16:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alunos', '0002_auto_20170815_1801'),
    ]

    operations = [
        migrations.CreateModel(
            name='DiasSemana',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=20, verbose_name='Dia')),
            ],
        ),
        migrations.RemoveField(
            model_name='aluno',
            name='dias_utilizacao',
        ),
        migrations.AddField(
            model_name='aluno',
            name='dias_utilizacao',
            field=models.ManyToManyField(to='alunos.DiasSemana'),
        ),
    ]
