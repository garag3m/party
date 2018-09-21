from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [

	# Inicio
    path('',views.IndexView.as_view(),name='index'),

    # Lista e Detalhes do evento
    path('eventos/',views.BuscarEventoList.as_view(), name='eventos-lista'),
    path('eventos/<pk>/',views.BuscarEvento.as_view(), name='eventos-detalhes'),
    path('eventos/<pk>/album/',views.VisualizaAlbum.as_view(), name='eventos-album'),
]
