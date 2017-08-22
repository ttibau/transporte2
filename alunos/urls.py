from django.conf.urls import url 
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
	url(r'^index', views.index, name= 'index'),  
	url(r'^login', views.do_login, name= 'login'), 
	url(r'^logout', views.do_logout, name= 'logout'),
	url(r'^novo-aluno', login_required(views.NovoAluno.as_view(success_url='/index')), name= 'novo-aluno'),
	url(r'^novo-chamado', login_required(views.NovoChamado.as_view(success_url='/index')), name= 'novo-chamado'),
	url(r'^(?P<pk>[-\w]+)/$', login_required(views.AlunoView.as_view()), name='aluno-detalhe'),
	url(r'^(?P<pk>[-\w]+)/delete$', login_required(views.AlunoDelete.as_view()), name='aluno-delete'),
	url(r'^(?P<doc_id>[-\w]+)/doc/valida$', views.valida_documento, name='valida-cpf'),

	
]