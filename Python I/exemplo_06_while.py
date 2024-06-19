import os

def exemplo_meu():
    apresentar_menu()
    menu_escolhido = int(input("Digite o menu escolhido: "))
    limpar_tela()

    # Enquanto o meu escolhido for defirente de sair(20),repetir
    while menu_escolhido != 20:
        # Se o menu escolhi for 1, então executará o exemplo de números
        if menu_escolhido == 1:
            exemplo_numeros()
        # Senão se o menu escolhido for 2, então executará o exemplo de supermercado
        elif menu_escolhido == 2:
            exemplo_supermercado()
        elif menu_escolhido == 3:
            descobrir_maior_valor()
        elif menu_escolhido == 4:
            descobrir_menor_quantidade_kg_mel()
        
        apresentar_menu()
        menu_escolhido = int(input("Digite o menu escolhido: "))
        limpar_tela()


def limpar_tela():
    os.system("cls")


def apresentar_menu():
    print("|------------------------------------------------------------|")
    print("|                       SISTEMA PROWAY                       |")
    print("|------------------------------------------------------------|")
    print("|  1 - Exemplo de números                                    |")
    print("|  2 - Exemplo de supermercado                               |")
    print("| 20 - sair                                                  |")
    print("|------------------------------------------------------------|")


def exemplo_numeros():
    indice, soma_numeros = 0, 0
    while indice < 5:
        numero = int(input("Digite um número: "))
        soma_numeros = soma_numeros + numero
        # Incrementa a variável indice em 1
        indice = indice + 1
    medida = soma_numeros / 5
    print("Soma: ", soma_numeros)
    print("Média: ", medida)


def exemplo_supermercado():
    deseja_cadastrar, total = "", 0
    while deseja_cadastrar != "não":
        nome_produto = input("Digite o nome do produto: ").strip() # min: 2 - max: 40
        # enquanto o nome do produto conter menos de 2 caracter ou mais de 40, irá
        # solicitar o nome novamente
        while len(nome_produto) < 2 or len(nome_produto) > 40:
            print("Nome do pro inválido! Mínimo 2 caracteres e máximo 40")
            nome_produto= input("Digite o nome do produto: ").strip() # min: 2 max: 40
        
        quantidade = int(input("Digite a quantidade: "))
        while quantidade <= 0:
            print("Quantidade inválida! Mínimo de uma unidade")
            quantidade = int(input("Digite a quantidade: "))
        
        preco_unitario = float(input("Digite o preço unitário: ").replace(",", "."))
        while preco_unitario <= 0:
            print("Preço unitário inválido! Preço mínimo de R$ 0,01")
            preco_unitario = float(input("Digite o preço unitário: ").replace(",", "."))
        
        total_parcial = quantidade * preco_unitario
        total = total + total_parcial
        print("Total parcial: ", total_parcial, end="\n\n")

        deseja_cadastrar = input("Deseja cadastrar outro? [sim/não] ".strip())
    print("total: ", total)

def descobrir_maior_valor():
    indice = 0
    maior_salario = 0
    while indice < 10:
        salario = float(input("Digite o salário: "))
        if salario > maior_salario:
            maior_salario = salario
        indice = indice + 1
    print("Maior salário: ", maior_salario)


def descobrir_menor_quantidade_kg_mel():
    indice = 0
    menor_quantidade_mel = 2_147_483_647
    while indice < 3:
        quantidade_mel = int(input("Digite a quantidade de mel vendida: "))
        if quantidade_mel < menor_quantidade_mel:
            menor_quantidade_mel = quantidade_mel
        indice = indice + 1
    print("Menor quantidade de mel: ", menor_quantidade_mel)



#https://github.com/franciscosensaulas/proway-2024-04-logica-i/blob/main/L%C3%B3gica%20I/Exerc%C3%ADcios/Lista%2003%20-%20Enquanto.pdf

# 1. Solicite o nome, preço de 13 peças.

def exercicio01():
    indice, preco_peca = 0, 0
    while indice <= 12:
        nome = input("Digite o nome da peça: ")
        preco = float(input("Digite o preço: ").replace(",", "."))
        if preco < preco_peca:
            preco_peca = preco
        indice = indice + 1
        print("A peça", nome, "está custando: R$", preco)


# 2. Solicite a idade para o usuário enquanto que a idade for menor que 128.

def exercicio02():
    idade_usuario = 0
    idade = int(input("Digite a sua idade: "))
    while idade < 128:
        idade = int(input("Digite a sua idade: "))
        if idade > idade_usuario:
            idade_usuario = idade


# 3. Solicite nomes ao usuário até que o mesmo digite fim para o nome.

def exercicio03():
    nome_usuario = ""
    nome = input("Digite um nome: ")
    while nome != "fim":
        nome = input("Digite um nome: ")
        if nome != nome_usuario:
            nome_usuario = nome


# 4. Solicite o peso para o usuário até que o peso seja menor que 0 ou maior que 300,00. 
#    Apresentar ao final a quantidade de pessoas que informaram o peso.
            
def exercicio04():
    peso_usuario = 0
    peso = float(input("Digite o seu peso: ").replace(",", "."))
    while peso >= 0:
        if peso <= 300:
            peso = float(input("Digite o seu peso: ").replace(",", "."))
        elif peso >= peso_usuario:
            peso_usuario = peso

#https://dontpad.com/franciscosensaulas
exercicio04()