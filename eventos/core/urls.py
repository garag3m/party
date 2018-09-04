from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [

    path('',views.IndexView.as_view(),name='index'),
    path('eventos/',views.BuscarEventoList.as_view(), name='eventos-lista'),
    path('eventos/<slug>/',views.BuscarEvento.as_view(), name='eventos-detalhes'),
    path('eventos/<slug>/album/',views.VisualizaAlbum.as_view(), name='eventos-album'),
]
