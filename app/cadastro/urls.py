from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'cadastro'
urlpatterns = [

    path('',views.cadastro,name='cadastro'),

    # Login and Logout
    path('login/',auth_views.login, {'template_name': 'cadastro/login.html'},name='login'),
    path('logout/',auth_views.logout, {'next_page': 'core:index'}, name='logout'),

    # Dashboard
    path('dashboard/',views.Dashboard.as_view(),name='dashboard'),
]
