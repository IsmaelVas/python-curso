import os
from rich.console import Console
from rich.table import Table
import questionary

def exemplo_tabela():
    # Instanciando um objeto de Tabela
    tabela = Table(show_header=True)
    # Adicionando as colunas na tabela
    tabela.add_column("Modelo")
    tabela.add_column("Ano Fabricação")
    tabela.add_column("Preço")

    # Adicionando as linhas preenchendo o valor para cada uma das colunas
    tabela.add_row("Gol Quadrado", "1990", "R$ 14.900,00")
    tabela.add_row("Uno com escada", "1981", "R$ 9.530,00")

    # Instanciando um objeto de Console
    console = Console()
    # Apresentar a tabela
    console.print(tabela)


def limpar_tela():
    os.system("cls")


# Ex. 1: Criar um vetor para armazenar 6 e-mails e apresentar eles
    
def exercicio1():

    email = []
    for i in range(6):
        email.append(questionary.text("Digite o seu e-mail: ").ask().strip())
    
    for i in range(6):
        print("E-mail: ", email[i])


# Ex. 2: Criar vetores para armazenar nome, peso, altura. 
#           Preencher os vetores solicitando esses dados para o usuário.
#           Calcular o imc de cada um armazenando em outro vetor.
#           Apresentar nome e imc de cada registro armazenado nos vetores.
#           Solicitar para 3 pessoas.

def exercicio2():
    nome, peso, altura = [], [], []

    nome.append(questionary.text("Digite o seu nome: ").ask().strip())
    peso.append(float(questionary.text("Digite o seu peso: ").ask().strip().replace(",", ".")))
    altura.append(float(questionary.text("Digite o seu altura: ").ask().strip().replace(",", ".")))

    nome.append(questionary.text("Digite o seu nome: ").ask().strip())
    peso.append(float(questionary.text("Digite o seu peso: ").ask().strip().replace(",", ".")))
    altura.append(float(questionary.text("Digite o seu altura: ").ask().strip().replace(",", ".")))

    nome.append(questionary.text("Digite o seu nome: ").ask().strip())
    peso.append(float(questionary.text("Digite o seu peso: ").ask().strip().replace(",", ".")))
    altura.append(float(questionary.text("Digite o seu altura: ").ask().strip().replace(",", ".")))

    imc = []
    imc.append(peso[0] / (altura[0] * altura[0]))
    imc.append(peso[1] / (altura[1] * altura[1]))
    imc.append(peso[2] / (altura[2] * altura[2]))

    print(nome[0], "seu peso ideal é:", imc[0])
    print(nome[1], "seu peso ideal é:", imc[1])
    print(nome[2], "seu peso ideal é:", imc[2])

     #Criar a tabela adicionando o cabeçalho
    tabela = Table(show_header=True, show_lines=True)
    tabela.add_column("Nome")
    tabela.add_column("Peso")
    tabela.add_column("Altura")
    tabela.add_column("IMC")

    # Adicionar na tabela os dados dos alunos
    tabela.add_row(nome[0], format(peso[0], ".2f"), format(altura[0], ".2f"), format(imc[0], ".2f"))
    tabela.add_row(nome[1], format(peso[1], ".2f"), format(altura[1], ".2f"), format(imc[1], ".2f"))
    tabela.add_row(nome[2], format(peso[2], ".2f"), format(altura[2], ".2f"), format(imc[2], ".2f"))


    
    console = Console()
    console.print(tabela)


exercicio2()

""" Digite o seu e-mail: ismael@gmail.com
Digite o seu e-mail: Francisco@gmail.com
Digite o seu e-mail: Gustavo@gmail.com
Digite o seu e-mail: Jessica@gmail.com
Digite o seu e-mail: Renan@gmail.com
Digite o seu e-mail: Bernardo@gmail.com """