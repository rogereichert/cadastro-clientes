from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import ClienteForm
from .models import Cliente

def cliente_list(request):
    clientes = Cliente.objects.ativos()
    return render(request, "clientes/cliente_list.html", {"clientes": clientes})

def cliente_create(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            cliente = form.save()
            messages.success(request, f"Cliente '{cliente.nome}' cadastrado com sucesso.")
            return redirect("clientes:list")
        messages.error(request, "Corrija os dados do formulário. ")
    else:
        form = ClienteForm()
    return render(request, "clientes/cliente_form.html", {"form": form})