# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from alunos.models import Aluno, Chamado, TipoChamado, DiasSemana, DocumentoCPF, DocumentoRG, Cidade

# Register your models here.
admin.site.register(Aluno)
admin.site.register(Chamado)
admin.site.register(TipoChamado)
admin.site.register(DiasSemana)
admin.site.register(DocumentoCPF)
admin.site.register(DocumentoRG)
admin.site.register(Cidade)


