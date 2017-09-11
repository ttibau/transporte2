# -*- coding: utf-8 -*-
from django import forms
from alunos.models import Aluno, Chamado

class AlunoForm(forms.ModelForm):

	class Meta():

		model = Aluno
		fields = [
			'nome', 'rg', 'titulo', 'cpf', 'email', 'cep', 'endereco', 'bairro', 'mora_com_pais',
			'telefone_fixo', 'telefone_movel', 'registro_academico', 'tem_whatsapp', 'inst_ensino_nome',
			'inst_ensino_cicade', 'curso', 'duracao_curso', 'semestre_matriculado', 'turno', 'servicos',
			'situacao', 'dias_utilizacao', 'foto'
		]
		widgets = {
			'nome' : forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Nome completo'}),
			'rg' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'RG'}),
			'titulo' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Título de eleitor'}),
			'cpf' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Número do CPF'}),
			'email' : forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'E-mail'}),
			'cep' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'CEP'}),
			'endereco' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Endereço'}),
			'bairro' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Bairro'}),
            'mora_com_pais' : forms.CheckboxInput(attrs={'class' : 'form-control flat'}),
			'telefone_fixo' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Telefone fixo'}),
			'telefone_movel' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Telefone móvel'}),
			'registro_academico' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Registro acadêmico'}),
			'tem_whatsapp' : forms.CheckboxInput(attrs={'class' : 'form-control flat'}),
			'inst_ensino_nome' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Instituição de ensino'}),
			'inst_ensino_cicade' : forms.Select(attrs={'class' : 'form-control'}),
			'curso' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Curso'}),
			'duracao_curso' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Duração do curso (anos)'}),
			'semestre_matriculado' : forms.CheckboxInput(attrs={'class' : 'form-control flat'}),
			'turno' : forms.Select(attrs={'class' : 'form-control'}),
			'servicos' : forms.Select(attrs={'class' : 'form-control'}),
            'situacao' : forms.Select(attrs={'class' : 'form-control'}),
            'dias_utilizacao' : forms.CheckboxSelectMultiple(attrs={'class' : 'form-control flat'}),
            'foto' : forms.FileInput()
		}


class ChamadoForm(forms.ModelForm):

	class Meta():

		model = Chamado
		fields = [
			'tipo',  'aluno', 'titulo', 'texto' 
		]
		widgets = {
			'tipo' : forms.Select(attrs={'class' : 'form-control'}),
			#'usuario' : forms.Select(attrs={'class' : 'form-control'}),
			'aluno' : forms.Select(attrs={'class' : 'form-control'}),
			'titulo' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Título'}),
			'texto' : forms.Textarea(attrs={'class' : 'form-control', 'placeholder' : 'Texto', 'rows': 11})
		}

