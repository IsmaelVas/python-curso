def exemplo01():
    numero = int(input("Digite um número: "))
    # Comparar se o número informado é o 10
    if numero == 10: # se
        print("é o número 10")
    else: # senão
        print("é diferente do número 10")


    # Operadores relacionais
    # =		Igual
    # >		Maior que
    # >=	Maior ou igual que
    # < 	Menor que
    # <=	Menor ou igual que
    # !=	Diferente


def exemplo02():
    ano_nascimento = int(input("Digite o seu ano de nascimento: "))
    if ano_nascimento > 2010:
        print("Geração alpha")
    elif ano_nascimento > 1998:
        print("Geração z")
    elif ano_nascimento > 1981:
        print("Geração y")
    elif ano_nascimento > 1961:
        print("Geração x")
    else:
    	print("Baby boomers")

def exemplo03():
    # nome de dois produtos
    # quantidade de dois produtos
    # preço de cada dos produtos
    # Calcular e aplicar desconto
    # solicitar pagamento a vista ou a prazo
    # se for pagamento a vista dar desconto de 5%, caso contrário questionar a quantidade de parcelar
    # se a quantidade de parcelas for maior que 10, acrescentar 18% no valor total

    produto1 = input("Digite o nome do produto: ")
    quantidade1 = int(input("Digite a quantidade: "))
    preco_unitario1 = float(input("Digite o preço unitário: "))

    produto2 = input("Digite o nome do produto: ")
    quantidade2 = int(input("Digite a quantidade: "))
    preco_unitario2 = float(input("Digite o preço unitário: "))

    produto1_total_parcial = quantidade1 * preco_unitario1
    produto2_total_parcial = quantidade2 * preco_unitario2

    total_compra = produto1_total_parcial + produto2_total_parcial

    forma_pagamento = int(input("Escolha a forma de pagamento: \n1 - A vista \n2 - A prazo\nEscolha: "))
    if forma_pagamento == 1:
        valor_desconto = total_compra * 0.05 # calcular 5% de desconto
        valor_a_ser_pago = total_compra - valor_desconto
        print("O valor total da compra é: R$", total_compra)
        print("Valor do desconto é: R$", valor_desconto)
        print("Valor total a ser pago é: R$", valor_a_ser_pago)
    elif forma_pagamento == 2: # verificando a forma de pagamento que é a prazo
        quantidade_parcelas = int(input("Informe a quantidade de parcelas: "))
        if quantidade_parcelas <= 10:
            print("O valor total a ser pago é: R$", total_compra)
        else:
            valor_acrescimo = total_compra * 0.18 # calculando 18% do total da compra
            valor_a_ser_pago = total_compra + valor_acrescimo
            valor_cada_parcela = valor_a_ser_pago / quantidade_parcelas
            print("O valor total da compra é: R$", total_compra)
            print("O valor do juros é: R$", valor_acrescimo)
            print("O valor total a ser pago é: R$", valor_a_ser_pago)
            print("O valor de cada parcela é: R$", valor_cada_parcela)

def exemplo04():
    login = input("Digite o login: ")
    senha = input("Digite a senha: ")
    # Verificando que o login é admin e a senha é 1234
    if login == "admin" and senha == "1234":
        print("Autenticado, seja bem vindo!")
    else:
        print("Login e/ou senha inválida")
    # Tabela verdade
    # V e V => V
    # F e V => F
    # V e F => F
    # F e F => F


def exemplo05():
    nome = input("Digite o nome do produto: "). strip()
    produto_vencido_texto= input("Produto vencido? [sim/não]: ").strip().lower()
    # Fazendo a sanitização da string (substituido ',' por '.' e 'R$' por ''(nada))
    preco_unitario = float(input("Digite o preço unitário: R$ ").replace(",", ".").replace("R$", ""))
    
    # verificar se o usuário 'sim', 's', 'y', 'yes'. Caso positivo o produto é considerado positivo
    if produto_vencido_texto == "sim" or produto_vencido_texto == "yes":
        produto_vencido = True
    else:
        produto_vencido = False
    # Tabel Verdade
    # V ou V => V
    # F ou V => V
    # V ou F => V
    # F ou F => F


def exemplo06par():
    numero = int(input("Digite um número: "))
    if numero % 2 == 0:
        print("PAR")


def exemplo07impar():
    numero = int(input("Digite um número: "))
    if numero % 2 != 0:
        print("ÍMPAR")


# Ex. 01: Solicite o nome, peso, altura, calcule o imc e a apresentar a classificação (buscar tabela no google)

def exercicio01():
    nome = input("Digite o seu nome: ")
    peso = float(input("Digite o seu peso: ").replace(",", "."))
    altura = float(input("Digite a sua altura: ").replace(",", "."))
    imc = peso / (altura * altura)
    
    if imc < 18.5:
        print("Abaixo do peso")
    elif imc >= 18.5 and imc <= 24.99:
        print("Peso ideal")
    elif imc >= 25 and imc <= 29.99:
        print("Levemente acima do peso")
    elif imc >= 30 and imc <= 34.99:
        print("Obsidade grau I")
    elif imc >= 35 and imc <= 39.99:
        print("Obsidade grau II")
    elif imc > 40:
        print("Obsidade grau III")


# Ex. 02: Solicite os 3 lados e apresentar se é um triangulo equilatero, isósceles, escaleno

def exercicio02():
    lado1 = float(input("Digite o primeiro lado: ").replace(",", "."))
    lado2 = float(input("Digite o segundo lado: ").replace(",", "."))
    lado3 = float(input("Digite o terceiro lado: ").replace(",", "."))
    if lado1 == lado2 and lado1 == lado3:
        print("Triangulo Equilátero")
    elif lado1 == lado2 and lado1 != lado3:
        print("Triangulo Isósceles")
    elif lado1 == lado3 and lado1 != lado2:
        print("Triangulo Isósceles")
    elif lado2 == lado3 and lado1 != lado2:
        print("Triangulo Isósceles")
    elif lado1 != lado2 and lado1 != lado3:
        print("Triangulo Escaleno")    


# Ex. 03: Solicite 3 notas, apresente a média e o status(reprovado, em exame, aprovado)

def exercicio03():
    nota1 = float(input("Digite a primeira nota: ").replace(",", "."))
    nota2 = float(input("Digite a sugunda nota: ").replace(",", "."))
    nota3 = float(input("Digite a terceira nota: ").replace(",", "."))
    media = (nota1 + nota2 + nota3) / 3
    if media >= 7:
        print("Aprovado")
    elif media >= 5 and media <=6.5:
        print("Em exame")
    elif media < 5:
        print("Reprovado")


# Ex. 04: Solicite um caracter e apresente se é vogal ou consoante

def exercicio04():
    letra = input("Digite uma letra: ")
    if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
        print("Letra digitada é (", letra, ") ela é uma vogal")
    else:
        print("Letra digitada é (", letra, ") ela é uma consoante")


# Ex. 05: Solicite um número e apresente se é positivo, negativo ou neutro.

def exercicio05():
    numero = float(input("Digite um número: ").replace(",", "."))
    if numero == 0:
        print("Neutro")
    elif numero > 0:
        print("Positivo")
    elif numero < 0:
        print("Negativo")


# Ex. 06: Solicite um número e apresente se é ímpar ou par

def exercicio06():
    numero = float(input("Digite um número: ").replace(",", "."))
    if numero % 2 == 0:
        print("Número digitado é par")
    else:
        print("Número digitado é ímpar")


# Ex. 07: Solicite um número e apresente se é maior que 8000

def exercicio07():
    numero = float(input("Digite um número: ").replace(",", "."))
    if numero > 8000:
        print(numero, "é maior que 8000")


# Ex. 08: Solciite a idade e apresente se é bebê, criança, adolescente, adulto ou idoso

def exercicio08():
    idade = int()



exercicio07()

#Link para GitHub: https://bit.ly/4aHAVB8

# Ex. 08: Solciite a idade e apresente se é bebê, criança, adolescente, adulto ou idoso
# Ex. 09: Solicite 3 números e apresente qual o menor e qual o maior
# Ex. 10: Solicite 3 números e apresente em ordem crescente
# Ex. 11: Solicite 3 números e apresente em ordem decrescente
# Ex. 12: Solicite os seguintes dados e realize a conversão da temperatura:
#           - Temperatura
#           - Temperatura origem
#           - Temperatura destino
#        Temperaturas suportadas: Celsius, Fahrenheit e Kelvin
