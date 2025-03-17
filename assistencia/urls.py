from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_aparelhos, name='lista_aparelhos'),
    path('obter_modelos/', views.obter_modelos, name='obter_modelos'),
]
