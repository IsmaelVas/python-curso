from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

def index(request) -> HttpResponse:
    response = HttpResponse(content="""
                    <style>body{
                    background-color: black;
                    color: rebeccapurple;}</style>
                    <h1>Olá Mundo!!</h1>
                    <a href="contato">Contato</a>
                    <br><br>
                    <a href="/exemplos-basicos/jogo">Jogo</a>
                    <br><br>
                    <a href="calculadora">Calculadora</a>
                    <br><br>
                    <a href="calculadora-form">Calculadora Form</a>
                    <br><br>
                    <a href="sobre">Sobre</a>
                    <br><br>
                    <a href="sobre-form">Sobre Form</a>
                    <br><br>
                    <a href="cadastro-carro-form">Cadastro de carros</a>
                    <br><br>
                    """)
    return response


def contato(request) -> HttpResponse:
    # Obteve o arquivo contato.html e armazenou na variável template
    template = loader.get_template(template_name="contato.html")
    # Renderizar o template armazenado na variável html
    #                        nomeando      nomeando
    html = template.render(context={}, request=request)
    respose = HttpResponse(content=html)
    return respose


def jogo(request) -> HttpResponse:
    return render(request, "jogo.html")


def calculadora(request, numero1: int=3, numero2: int=8) -> HttpResponse:
    soma = numero1 + numero2
    contexto_dados = {
        "n1": numero1,
        "n2": numero2,
        "soma": soma
    }
    return render(request, "calculadora.html", context=contexto_dados)


def calculadora_form(request) -> HttpResponse:
    return render(request, "calculadora-form.html",)


def calcular(request):
    numero1 = int(request.GET.get("numero1"))
    numero2 = int(request.GET.get("numero2"))
    operacao = request.GET.get("operacao")

    match(operacao):
        case "somar": resultado = numero1 + numero2
        case "subtrair": resultado = numero1 - numero2
        case "multiplicar": resultado = numero1 * numero2
        case "dividir": resultado = numero1 / numero2
    return HttpResponse(f"Resultado: {resultado}")
# Criar rota sobre com os seguintes dados no html
#   Nome (aluno escolhe o nome)
#   Sobrenome (aluno escolhe)
#   Nome completo (gerar o nome completo)
#   Idade (aluno escolhe)
#   Ano de Nascimento (gerar o ano nascimento)
#   Peso (aluno escolhe)
#   Altura (Aluno escolhe)
#   Imc (gerar o imc)
#   Imagem

def sobre(request) -> HttpResponse:
    return render(request, "sobre.html")


def sobre_form(request) -> HttpResponse:
    return render(request, "sobre-form.html")


def mandar(request):
    nome = request.GET.get("nome")
    sobrenome = request.GET.get("sobrenome")
    nome_completo = nome + " " + sobrenome
    idade = int(request.GET.get("idade"))
    ano_nascimento = 2024 - idade
    peso = float(request.GET.get("peso"))
    altura = float(request.GET.get("altura"))
    imc = peso / (altura * altura)
    mudar = {
        "nome_completo": nome_completo,
        "ano_nascimento": ano_nascimento,
        "peso": peso,
        "altura": altura,
        "imc": imc
    }
    return render(request, "sobre.html", context=mudar)
    return HttpResponse(f"Nome completo: {nome} {sobrenome} <br> Ano de nascimento: {2024 - idade} <br> Peso: {peso} <br> Altura: {altura} <br> IMC: {imc}","mudar.html")


def cadastro_carro(request):
    return render(request, "cadastro-carro-form.html")

def carro_cadastrado(request):
    modelo = request.POST.get("modelo")
    preco = request.POST.get("preco")
    ano_fabricacao = request.POST.get("ano_fabricacao")
    cor = request.POST.get("cor")

    match(cor):


    cadastrar = {
        "modelo": modelo,
        "preco": preco,
        "ano_frabricacao": ano_fabricacao,
    }