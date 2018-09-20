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
]
