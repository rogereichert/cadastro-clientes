from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, redirect

from .forms import ClienteForm
from .models import Cliente

def cliente_list(request):
    q = (request.GET.get("q") or "").strip()
    page_number = request.GET.get("page", 1)

    clientes_qs = Cliente.objects.ativos()

    if q:
        clientes_qs = clientes_qs.filter(
            Q(nome__icontains=q)
            | Q(documento__icontains=q)
            | Q(email__icontains=q)
            | Q(telefone__icontains=q)
        )

    paginator = Paginator(clientes_qs, 10)
    page_obj = paginator.get_page(page_number)
    return render(
        request,
        "clientes/cliente_list.html",
        {
            "clientes": page_obj.object_list,
            "page_obj": page_obj,
            "paginator": paginator,
            "q": q,
        },
    )

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

