from django.urls import path
from . import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("ordens/", views.ordens, name="ordens"),
    path("financeiro/", views.financeiro, name="financeiro"),
    path("login/", views.login_view, name="login"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("estoque/", views.estoque, name="estoque"),
    path("clientes/", views.clientes, name="clientes"),
    path("senhas/", views.clientes, name="senhas"),
    path("clientes/", views.clientes, name="clientes"),
    path("clientes/novo/", views.novo_cliente, name="novo_cliente"),
    path("clientes/editar/<int:id>/", views.editar_cliente, name="editar_cliente"),
    path("clientes/excluir/<int:id>/", views.excluir_cliente, name="excluir_cliente"),
]
