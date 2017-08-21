# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-15 18:01
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('alunos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chamados',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateTimeField(auto_now_add=True)),
                ('texto', models.TextField(max_length=1000)),
                ('aluno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alunos.Aluno')),
            ],
        ),
        migrations.CreateModel(
            name='TipoChamado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome do chamado')),
            ],
        ),
        migrations.AddField(
            model_name='chamados',
            name='tipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alunos.TipoChamado'),
        ),
        migrations.AddField(
            model_name='chamados',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
