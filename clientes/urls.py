from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('ordens/', views.ordens, name='ordens'),
    path('financeiro/', views.financeiro, name='financeiro'),
    path('login/', views.login_view, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('estoque/', views.estoque, name='estoque'),
    path('clientes/', views.clientes, name='clientes'),
]