from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from . import views

app_name = 'cadastro'
urlpatterns = [

    path('',views.cadastro,name='cadastro'),

    # Login and Logout
    path('login/',auth_views.login, {'template_name': 'cadastro/login.html'},name='login'),
    path('logout/',auth_views.logout, {'next_page': 'core:index'}, name='logout'),

    # Dashboard
    path('dashboard/',login_required(views.Dashboard.as_view()), name='dashboard'),

    # Minhas Inscrições
    path('dashboard/insc/', login_required(views.MyInsc.as_view()), name='inscricoes'),

    # Cadastrar Evento
    path('dashboard/cadastro-evento/',login_required(views.CadastraEvento.as_view()), name='cadastro-evento'),

    # Alterar Evento
    path('dashboard/alterar-evento/<pk>/',login_required(views.AlterarEvento.as_view()), name='alterar-evento'),

    # Excluir Evento
    path('dashboard/excluir-evento/<pk>/',login_required(views.evento_delete), name='excluir-evento'),

    # Retorno do alterar evento
    path('dashboard/retorno/',login_required(views.RetornoEvento.as_view()), name='alterar-retorno'),

    # Emitir certificado
    path('dashboard/emitir/',login_required(views.AutorizaView.as_view()), name='emitir'),

    # Erro
    path('dashboard/excluir-evento/<pk>/erro/',views.erro, name='erro'),

    # Publicar fotos
    path('dashboard/publicar-fotos/',login_required(views.PublicarFotos.as_view()), name='publicar'),

    # Atividade
    path('dashboard/atividade/',login_required(views.AtividadeEvento.as_view()), name='atividade'),

    # Noticias
    path('dashboard/noticias/',login_required(views.NoticiasView.as_view()), name='noticias'),

    # Meus certificados
    path('dashboard/certificado/', login_required(views.CertificadoView.as_view()), name='certificado'),
]
