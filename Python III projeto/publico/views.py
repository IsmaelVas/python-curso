from django.forms import model_to_dict
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render

from publico import models
from publico.forms import ClienteCadastroForm, ContatoCadastroForm

# Create your views here.
def cliente_cadastrar(request):
    if request.method == "POST":
        form = ClienteCadastroForm(request.POST)
        if form.is_valid():
            cliente = form.save()
            return redirect("cliente_detalhe", id=cliente.id)
    
    form = ClienteCadastroForm()
    contexto = {"form": form}
    return render(request, "clientes/cadastrar.html", contexto)


def cliente_detalhe(request, id: int):
    cliente = get_object_or_404(models.Cliente, id=id)
    contatos = cliente.get_contatos()

    form_contato = ContatoCadastroForm()

    contexto = {"cliente": cliente, "contatos": contatos, "form_contato": form_contato}
    return render(request, "clientes/detalhe.html", contexto)


def contato_cadastrar(request, id_cliente: int):
    # Consultar o cliente por id ou retornar um 404 para o cliente
    cliente = get_object_or_404(models.Cliente, id=id_cliente)
    # Construir o form do contato com os dados preenchidos na tela
    form = ContatoCadastroForm(request.POST)
    # Construir o objeto de models.Contato, não persistindo os dados no banco de dados
    contato = form.save(commit=False) # Criando o objeto do models.Contato
    # Vincular o objeto ao contato
    contato.cliente = cliente
    # Persistir i contato no banco de dados
    contato.save()
    # Redirecionar para a tela de detalhe do cliente
    return redirect("cliente_detalhe", id=cliente.id)


def contato_editar(request, id: int):
    pass


def contato_apagar(request, id: int):
    contato = get_object_or_404(models.Contato, id=id)
    id_cliente = contato.cliente.id
    contato.delete()
    return redirect("cliente_detalhe", id=id_cliente)


def contato_detalhe(request, id: int):
    contato = get_object_or_404(models.Contato, id=id)
    return JsonResponse(model_to_dict(contato))


def endereco_cadastrar(request):
    pass


def endereco_editar(request, id: int):
    pass


def endereco_apagar(request, id: int):
    pass

