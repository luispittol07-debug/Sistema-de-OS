from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Cliente, OrdemServico
from .forms import ClienteForm
from django.db.models import Q


@login_required
def senhas(request):
    return render(request, "senhas.html")


@login_required
def estoque(request):
    return render(request, "estoque.html")


@login_required
def ordens(request):
    return render(request, "ordens.html")


@login_required
def is_tecnico(user):
    return user.groups.filter(name="tecnico").exists()


@login_required
def financeiro(request):
    return render(request, "financeiro.html")


def login_view(request):
    erro = None
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
        else:
            erro = "Usuário não encontrado!"
    return render(request, "login.html", {"erro": erro})


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


@login_required
def clientes(request):

    busca = request.GET.get("busca")

    if busca:
        clientes = Cliente.objects.filter(
            Q(nome__icontains=busca)
            | Q(telefone__icontains=busca)
            | Q(cpf_cnpj__icontains=busca)
        )
    else:
        clientes = Cliente.objects.all()

    context = {"clientes": clientes}

    return render(request, "clientes.html", context)


def novo_cliente(request):

    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("clientes")

    else:
        form = ClienteForm()

    return render(request, "cliente_form.html", {"form": form})


def editar_cliente(request, id):

    cliente = get_object_or_404(Cliente, id=id)

    if request.method == "POST":
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect("clientes")

    else:
        form = ClienteForm(instance=cliente)

    return render(request, "cliente_form.html", {"form": form})


def excluir_cliente(request, id):

    cliente = get_object_or_404(Cliente, id=id)
    cliente.delete()

    return redirect("clientes")
