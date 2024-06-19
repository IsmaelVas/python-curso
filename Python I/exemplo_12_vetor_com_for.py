import questionary
from rich.table import Table
from rich.console import Console
import os


def exemplo_frutas():
    frutas = []

    # Criando um for para solicitar o nome de 4 frutas e adicionando no vetor
    for i in range(4):
        frutas.append(questionary.text("Digite o nome da fruta: ").ask().strip())
    
    # Apresentar as frutas, iterando o vetor
        for i in range(4):
            print(frutas[i])

def exemplo_alunos():
    #Criando 4 vetores, um para o nome dos alunos, nota1 dos alunos...
    nomes, notas1, notas2, notas3 = [], [], [], []
    # Solicitar a quantidade de alunos que deseja cadastrar
    quantidade_alunos = int(questionary.text("Digite a quantidade de alunos para cadastro: ").ask().strip())
    # Solicitar os dados de cada um dos alunos
    for i in range(quantidade_alunos):
        nomes.append(questionary.text("Digite o nome do aluno: ").ask().strip())
        notas1.append(solicitar_nota("Digite a primeiro nota: "))
        notas2.append(solicitar_nota("Digite a segunda nota: "))
        notas3.append(solicitar_nota("Digite a terceira nota: "))
    
    medias = []
    # Calcular a média de cada aluno
    for i in range(quantidade_alunos):
        nota1 = notas1[i]
        nota2 = notas2[i]
        nota3 = notas3[i]
        media = (nota1 + nota2 + nota3) / 3
        medias.append(media)
    
    #Criar a tabela adicionando o cabeçalho
    tabela = Table(show_header=True, show_lines=True)
    tabela.add_column("Aluno")
    tabela.add_column("Nota 1")
    tabela.add_column("Nota 2")
    tabela.add_column("Nota 3")
    tabela.add_column("Média")

    # Adicionar na tabela os dados dos alunos
    for i in range(quantidade_alunos):
        tabela.add_row(
            nomes[i],
            formatar_nota(notas1[i]),
            formatar_nota(notas2[i]),
            formatar_nota(notas3[i]),
            formatar_nota(medias[i])
            )
    
    console = Console()
    console.print(tabela)

def solicitar_nota(texto: str) -> float:
    nota = float(questionary.text(texto).ask().strip().replace(",", "."))

    while nota < 0 or nota > 10:
        print("Nota inválida! Deve ser entre 0 e 10")
        nota = float(questionary.text(texto).ask().strip().replace(",", "."))
    
    return nota

# Oque fica dentro dos parenteses se chama parâmetro
def formatar_nota(nota: float) -> str:
    nota_formatada = format(nota, ".2f").replace(",", ".")
    return nota_formatada


# Ex. 1: Criar um vetor de nomes e solicitar para o usuário 4 nomes, apresentar eles depois de solicitar
# Ex. 2: Criar um vetor de nome do jogo, quantidade e preço unitário para 4 produtos, 
#       calcular o valor de cada um deles armazenando em outro vetor. Listar todos os produtos depois
exemplo_alunos()
