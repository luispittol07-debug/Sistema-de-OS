from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test

def clientes(request):
    return render(request,'clientes.html')

@login_required
def dashboard(request):
    return render(request, "dashboard.html")

@login_required
def cadastro(request):
    return render(request, "cadastro.html")

@login_required
def ordens(request):
    return render(request, "ordens.html")

def is_tecnico(user):
    return user.groups.filter(name='tecnico').exists()

@user_passes_test(is_tecnico)
def financeiro(request):
    return render(request, "financeiro.html")

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('Admin')
        password = request.POST.get('admin1234')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            if user.is_superuser:
                return redirect('/admin/')
            else:
                return redirect('dashboard')

    return render(request, 'login.html')