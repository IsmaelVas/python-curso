import questionary
import os
import time

def exemplo01():
    # Para indice de 0 até 10 faça
    # Começa no 0 para no 11
    for indice in range (0, 11):
        print(indice)


def exemplo_solicitar_numeros():
    # Para indice de 0 até 4 faço
    # Começar no 0 e parar no 5
    soma_numeros = 0
    for indice in range(5):
        numero = int(input("Digite um número [" + str(indice + 1) + "/5]: "))
        # acumular a váriavel número na samo
        soma_numeros = soma_numeros + numero
    print("Soma dos números: ", soma_numeros)


def exemplo_pokedex():
    # Abrir o arquivo de csv no modo de adição e leitura, e coloca o cursor no final do arquivo
    arquivo = open("pokedex.csv", mode=("a+"))
    # Mudar o cursor para o começo do arquivo, para que seja possível ler o conteúdo dele
    arquivo.seek(0)
    # Ler todos as linhas do arquivo
    linhas_aquivo = arquivo.readlines()

    print("Pokemons cadastrados: ")
    # Percorrer cada um dos pokemons cadasrados(linhas)
    for indice in range(len(linhas_aquivo)):
        linha = linhas_aquivo[indice]
        linha = linha.replace(";", " => ")
        print(linha, end="")
    
    quantidade_pokemons_desejada = int(questionary.text("Digite a qantidade de pokemons desejada para cadastrar: ").ask())
    for indice in range(quantidade_pokemons_desejada):
        pokemon_nome = questionary.text("Digite o nome do pokemon").ask()
        pokemon_tipo = questionary.select("Escolha o tipo do pokemon: ", ["Água", "Fogo", "Terra", "Planta"]).ask()
        pokemon_codigo = int(questionary.text("Digite o código do pokemon").ask())
        linha = pokemon_nome + ";" + pokemon_tipo + ";" + str(pokemon_codigo) + "\n"
        arquivo.write(linha)
    
    arquivo.close()


def exemplo_contagem_regressiva():
    # renge(inicio, valor para parar, quantidade de incremento/descremento)
    for indice in range(10, -1, -1):
        print(indice)
        # Delay de 1 segundo, necessário importar time (import time)
        time.sleep(1)


# Ex. 1: Solicitar o nome, idade de 4 pessoas utilizando comando for

def exercicio01():
    for indice in range(4):
        nome = input("Digite o seu nome: ")
        idade = int(input("Digite a sua idade: "))
        indice = indice + 1


# Ex. 2: Solicitar nome do curso, carga horária, valor do curso e apresentar o valor por hora do curso. 
#        Questionar os dados de 2 cursos

def exercicio02():
    for indice in range(2):
        curso = input("Digite o nome do curso: ")
        hora = int(input("Digite a carga horaria: "))
        valor = float(input("Digite o valor do curso: ")) 
        valor_por_hora = valor / hora
        print("O valor por horá do curso", curso, "é", valor_por_hora)
        indice = indice + 1


# Ex. 3: Apresentar os números pares até 1000

def exercicio03():
    for indice in range(0, 1001, 1):
        if indice % 2 == 0:
            print(indice)


def exercicio04():
    for indice in range(0, 1001, 2):
        print(indice)

os.system("cls")
exemplo_pokedex()