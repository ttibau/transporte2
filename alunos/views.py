# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Aluno, Chamado, DiasSemana, DocumentoCPF, DocumentoRG
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.detail import DetailView
from django.core.urlresolvers import reverse_lazy
from .forms import AlunoForm, ChamadoForm
from django.views import View
# Create your views here.


class AlunoUpdate(UpdateView):
	model = Aluno
	template_name = 'app/update_aluno.html'
	form_class = AlunoForm


"""
	Método que vai colocar o is_active do aluno para false
"""
@login_required
def apaga_aluno(request, aluno_id):
	aluno = Aluno.objects.filter(pk=aluno_id)
	print (aluno)
	for field in aluno:
		field.is_active = False
		field.save()
	return redirect('/index')


""" 
	Método que vai modificar o status do documento
"""
@login_required
def modifica_documento(request, documentoTipo, doc_id, bool):
	print (bool)
	tipo = eval(documentoTipo.encode('utf8'))

	documento_id = int(doc_id)
	documento = tipo.objects.filter(pk=documento_id)
	for doc in documento:
		doc.is_valid = bool
		doc.save()
	return redirect('/index')


@login_required
def index(request):
	user = request.user
	alunos = Aluno.objects.all()
	alunos_manha = Aluno.objects.filter(turno='M')
	alunos_tarde = Aluno.objects.filter(turno='T')
	alunos_noite = Aluno.objects.filter(turno='N')
	count_alunos = alunos.count

	dict = {
		'user' : user,
		'alunos' : alunos,
		'count_alunos' : count_alunos,
		'count_alunos_manha' : alunos_manha.count,
		'count_alunos_tarde' : alunos_tarde.count,
		'count_alunos_noite' : alunos_noite.count
	}

	return render(request, 'app/index.html', dict)


def do_login(request):
	if(request.method == 'POST'):
		user = authenticate(username= request.POST['username'], password=request.POST['password'])
		if user is not None:
			login(request, user)
			return redirect('/index')
	return render(request, 'app/login.html')


def do_logout(request):
	logout(request)
	return redirect('/login')


class NovoAluno(CreateView):
	model = Aluno
	template_name = 'app/cadastro_aluno.html'
	form_class = AlunoForm


class NovoChamado(CreateView):
	model = Chamado
	template_name = 'app/cadastro_chamado.html'
	form_class = ChamadoForm

	def form_valid(self, form):
		form.instance.usuario = self.request.user
		return super(NovoChamado, self).form_valid(form)


class AlunoView(DetailView):
	model = Aluno
	template_name = 'app/detalhe_aluno.html'

	def get_context_data(self, **kwargs):
		context = super(AlunoView, self).get_context_data(**kwargs)
		context['chamados'] = Chamado.objects.filter(aluno = context['aluno'].id).order_by('-data')
		context['dias_utilizacao'] = DiasSemana.objects.filter(aluno=context['aluno'].id).order_by('-id')
		context['documento_cpf'] = DocumentoCPF.objects.filter(aluno=context['aluno'].id)
		context['documento_rg'] = DocumentoRG.objects.filter(aluno=context['aluno'].id)
		if context['aluno'].turno == 'M':
			context['turno_nome'] = 'Manhã'
		elif context['aluno'].turno == 'T':
			context['turno_nome'] = 'Tarde'
		elif context['aluno'].turno == 'N':
			context['turno_nome'] = 'Noite'
		elif context['aluno'].turno == 'MT':
			context['turno_nome'] = 'Manhã / Tarde'
		elif context['aluno'].turno == 'MTN':
			context['turno_nome'] = 'Manhã / Tarde / Noite'
		elif context['aluno'].turno == 'TN':
			context['turno_nome'] = 'Tarde / Noite'
		elif context['aluno'].turno == 'MN':
			context['turno_nome'] = 'Manhã / Noite'
		return context


class AlunoDelete(DeleteView):
	model = Aluno
	success_url = reverse_lazy('alunos:index')

	def get(self, *args, **kwargs):
		return self.post(*args, **kwargs)


