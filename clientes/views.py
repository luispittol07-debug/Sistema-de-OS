from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from .models import Cliente, OrdemServico


def clientes(request):
    return render(request, "clientes.html")


@login_required
def cadastro(request):
    return render(request, "cadastro.html")


@login_required
def ordens(request):
    return render(request, "ordens.html")


def is_tecnico(user):
    return user.groups.filter(name="tecnico").exists()


@user_passes_test(is_tecnico)
def financeiro(request):
    return render(request, "financeiro.html")


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            if user.is_superuser:
                return redirect("/admin/")
            else:
                return redirect("dashboard")

    return render(request, "login.html")


def dashboard(request):

    total_clientes = Cliente.objects.count()
    ordens_abertas = OrdemServico.objects.filter(status="aberta").count()
    ordens_concluidas = OrdemServico.objects.filter(status="concluida").count()

    context = {
        "total_clientes": total_clientes,
        "ordens_abertas": ordens_abertas,
        "ordens_concluidas": ordens_concluidas,
    }

    return render(request, "dashboard.html", context)
