import questionary
import os
import datetime


def exemplo_vetor_frutas():
    # Criando um vetor(Lugar para armazenar vários dados)
    frutas = []

    # Maçã é armazenado na primeira posição do vetor de frutas
    frutas.append("Maçã") #["Maçã"]
    frutas.append("Goiaba") #["Maçã", "Goiaba"]
    frutas.append("Tomate") #["Maçã", "Tomate", "Goiaba"]
    frutas.append("Banana") #["Maçã", "Tomate", "Goiaba", "Banana"]

    # Alterar o valor armazenado na primeira posição
    frutas[0] = "Apple" # ["Apple", "Tomate", "Goiaba", "Banana"]

    # Remover o valor Banana da posição 3
    frutas.remove("Banana")

    print("Frutas:")
    print(frutas[0])
    print(frutas[1])
    print(frutas[2])
    print(frutas)


def exemplo_notas():
    notas = []

    notas.append(float(questionary.text("Digite a primeria nota: ").ask()))
    notas.append(float(questionary.text("Digite a Segunda nota: ").ask()))
    notas.append(float(questionary.text("Digite a Terceira nota: ").ask()))

    soma = notas[0] + notas[1] + notas[2]
    media = soma / 3
    limpar_tela()

    print("Nota 01: ", notas[0])
    print("Nota 01: ", notas[0])
    print("Nota 01: ", notas[0])
    print("Média: ", media)


def exemplo_carros():
    carros, anos_fabricacao = [], []

    ano_atual = datetime.datetime.today().year
    #Gerar um vetor com os anos que o usuário pode escolher, como ano no de fabricação
    anos_disponiveis = [str(ano) for ano in range(1980, ano_atual + 1)]

    # input Entradas
    carros.append(questionary.text("Digite o modelo do carro").ask().strip())
    anos_fabricacao.append(int(questionary.select("Escolha o ano de fabricação: ", anos_disponiveis).ask()))

    carros.append(questionary.text("Digite o modelo do carro").ask().strip())
    anos_fabricacao.append(int(questionary.select("Escolha o ano de fabricação: ", anos_disponiveis).ask()))

    # Processamento
    idades = []
    idades.append(ano_atual - anos_fabricacao[0])
    idades.append(ano_atual - anos_fabricacao[1])

    # Output (Saída)
    limpar_tela()
    print("Modelo:", carros[0], "foi fabricado em:", anos_fabricacao[0], "idade:", idades[0])
    print("Modelo:", carros[1], "foi fabricado em:", anos_fabricacao[1], "idade:", idades[1])


def limpar_tela():
    os.system("cls")


exemplo_carros()