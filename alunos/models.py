# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class TipoChamado(models.Model):
    nome = models.CharField('Nome do chamado', max_length=100)

    def __str__(self):
        return self.nome.encode('utf-8')


class DiasSemana(models.Model):
    nome = models.CharField('Dia', max_length=20)
    

    def __str__(self):
        return self.nome.encode('utf-8')


class Aluno(models.Model):

    TURNO_CHOICES = (
        ('M', 'Manhã'),
        ('T', 'Tarde'),
        ('N', 'Noite'),
        ('MT', 'Manhã / Tarde'),
        ('MTN', 'Manhã / Tarde / Noite'),
        ('TN', 'Tarde / Noite'),
        ('MN', 'Manhã / Noite')

    )


    SITUACAO_CHOICES = (
        ('N', 'Novo'),
        ('R', 'Renovação')
    )

    SERVICOS_CHOICES = (
        ('FIES', 'FIES'),
        ('PROUNI', 'PROUNI'),
        ('PEP', 'PEP'),
        ('OUTROS', 'OUTRO (COLOCAR NA OBSERVAÇÃO)'),
        ('NENHUM', 'NENHUM')
    )


    # TELEFONES
    # Formato do telefone aceito: (99) 99999-9999
    # Outro formato aceito: (99) 9999-9999
    # regex="^(\(11\) [9][0-9]{4}-[0-9]{4})|(\(1[2-9]\) [5-9][0-9]{3}-[0-9]{4})|(\([2-9][1-9]\) [5-9][0-9]{3}-[0-9]{4})$", error_message=("Por favor, verifique o número informado.")
    # Adicionar um método que vai veirificar se o registro já existe no banco

    nome = models.CharField('Nome completo', max_length=100)
    rg = models.CharField('RG', max_length=11)
    titulo = models.CharField('Título de eleitor', max_length=50)
    cpf = models.CharField('CPF', max_length=15, blank=False)
    email = models.CharField('E-mail', max_length=34)
    cep = models.IntegerField('CEP', blank=False)
    endereco = models.CharField('Endereço', max_length=128)
    bairro = models.CharField('Bairro', max_length=20)
    mora_com_pais = models.BooleanField('Mora com os pais?')
    telefone_fixo =  models.CharField('Telefone fixo', max_length=13)
    telefone_movel = models.CharField('Telefone celular', max_length=13)
    registro_academico = models.CharField('Registro Acadêmico', max_length=20)
    tem_whatsapp = models.BooleanField('Tem Whatsapp?')
    inst_ensino_nome = models.CharField('Instituição de ensino', max_length=30)
    inst_ensino_cicade = models.CharField('Cidade da instituição', max_length=10)
    curso = models.CharField('Curso', max_length=25)
    duracao_curso = models.IntegerField('Duração do curso (Anos)')
    semestre_matriculado = models.BooleanField('Semestre atual matriculado')
    turno = models.CharField('Turno', max_length=2, choices=TURNO_CHOICES)
    servicos = models.CharField('Serviços', max_length=7, choices=SERVICOS_CHOICES, default='NENHUM')
    situacao = models.CharField('Situação', max_length=2, choices=SITUACAO_CHOICES)
    dias_utilizacao = models.ManyToManyField(DiasSemana)
    is_active = models.BooleanField('Está ativo?', default=True, blank=True)
    foto = models.FileField(blank=True, null=True)


    class Meta:
        ordering = ('nome', 'cpf', 'is_active')
        verbose_name = 'Aluno'
        verbose_name_plural = 'Alunos'


    def __unicode__(self):
        return self.nome

    def __str__(self):
        return self.nome + ' - ' + self.cpf


class Chamado(models.Model):
    tipo = models.ForeignKey(TipoChamado)
    usuario = models.ForeignKey(User)
    aluno = models.ForeignKey(Aluno)
    data = models.DateTimeField(auto_now_add=True)
    titulo = models.CharField('Título', max_length=100, default='')
    texto = models.TextField(max_length=1000)

    def __str__(self):
        return self.aluno.nome + ' - ' + str(self.data)


# Vai retornar a pasta com o id do usuario
def user_directory_path(instance, filename):
    return 'documentos_aluno_{0}/{1}'.format(instance.aluno.id, filename)


class DocumentoCPF(models.Model):
    aluno = models.ForeignKey(Aluno)
    arquivo = models.FileField(upload_to=user_directory_path)
    is_valid = models.BooleanField(default=False)
    data_inclusao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.aluno.nome

    def __unicode__(self):
        return self.aluno.nome

    class Meta:
        verbose_name = 'Documentação CPF'
        verbose_name_plural = 'Documentos - CPF'

class DocumentoRG(models.Model):
    aluno = models.ForeignKey(Aluno)
    arquivo = models.FileField(upload_to=user_directory_path)
    is_valid = models.BooleanField(default=False)
    data_inclusao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.aluno.nome

    class Meta:
        verbose_name = 'Documentação RG'
        verbose_name_plural = 'Documentos - RG'