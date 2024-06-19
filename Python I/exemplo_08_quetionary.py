# NÃO ESQUECER é necessario instalar o questionary
# Comando para instalar 'pip install questionary'
import questionary
import os
from typing import List

def exemplo_campo_texto() -> str:
    jogo = questionary.text("Qual o nome do jogo?").ask()
    return(jogo)


def exemplo_campo_senha() -> str:
    senha_conta_bancaria = questionary.password("Digite a senha da conta báncaria: ").ask()
    return(senha_conta_bancaria)


def exemplo_campo_select() -> str:
    tipo_jogo = questionary.select("Escolha o tipo de jogo: ", ["RPG", "FPS", "TIRO"]).ask()
    return(tipo_jogo)


def exemplo_campo_checkbox() -> List[str]:
    plataforma = questionary.checkbox("Escolha as plataformas que deseja comprar: ", ["PC", "PS5", "Xbox Series S/X", "Nitendo Switch"]).ask()
    return(plataforma)


def exemplo_campo_confirmacao() -> bool:
    confirma_compra = questionary.confirm("Deseja confirmar a compra?").ask()
    return(confirma_compra)


def exemplos():
    os.system("cls")
    nome_jogo = exemplo_campo_texto()
    print(nome_jogo)

    senha = exemplo_campo_senha()
    print(senha)
    
    tipo = exemplo_campo_select()
    print(tipo)
    
    plataforma = exemplo_campo_checkbox()
    print(plataforma)
    
    confirma_compra = exemplo_campo_confirmacao()
    print(confirma_compra)





exemplos()