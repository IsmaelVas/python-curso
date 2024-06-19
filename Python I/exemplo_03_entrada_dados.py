import datetime


def exemplo01():
    # input permite o usuário digitar algo que será armazenado dentro de uma variável
    email = input("Digite o seu e-mail: ")
    print(email)
    senha = input("Digite a sua senha: ")
   
    print(senha)
    print(email)


def exemplo02():
    idade = int(input("Digite a sua idade: "))
    # Obter o ano atual utilizando o momento atual, obtido através da classe datetime
    ano_atual = datetime.datetime.now().year
    # Calcular o ano de nascimento
    ano_nascimento = ano_atual - idade
    print("Ano de nascimento: ", ano_nascimento)


def exemplo03():
    nome = input("Digite o nome: ")
    sobrenome = input("Digite o sobrenome: ")
    nome_completo = (nome + " " + sobrenome)
    print("Nome completo: ", nome_completo)


def exemplo04():
    produto = input("Digite o nome do jogo: ")
    quantidade = int(input("Digite a quantidade: "))
    preco_unitario = float(input("Digite o preço unitário: "))
    preco = (quantidade * preco_unitario)
    print("Preço total: ", preco)


    # Exercício 01: Criar um algoritmo que solicite o nome, peso a altura
    #		Calcular o imc e apresentar o imc

def exercicio01():
    nome = input("Digite o seu nome: ")
    peso = float(input("Digite o seu peso (kg): "))
    altura = float(input("Digite a sua altura (m): "))
    imc = peso / (altura * altura)
    print("Peso ideal para o ", nome, "é ", imc)


    # Exercício 02: Criar um algoritmo que solicite nome, idade, nota 1, nota 2, nota 3
    #		Calcular a média (soma das notas / por quantidade de notas)

def exercicio02():
    nome = input("Digite o seu nome: ")
    idade = int(input("Digite a sua idade: "))
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a sugunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))
    media = (nota1 + nota2 + nota3) / 3
    print("O aluno", nome, "ficou com a média final igual a ", media)


    # Exercício 03: Criar um algoritmo que solicite os lados de um retangulo
    #		Calcular a área e apresentar

def exercicio03():
    altura_retangulo = float(input("Digite a altura do retangulo: "))
    largura_retangulo = float(input("Digite a largura do retangulo: "))
    area = altura_retangulo * largura_retangulo
    print("A área do retangulo é igual a: ", area)

exercicio03()