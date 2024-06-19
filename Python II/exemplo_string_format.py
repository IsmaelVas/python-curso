import os


def formatar_com_percentual(nome_usuario: str, idade_usuario: int, saldo_usuario: float):
    # %s é utilizando para string
    # %d é utilizando para int
    # %f é utilizando para float
    texto = "Bem vindo %s! Sua idade é %d você tem o saldo de %f" % (nome_usuario, idade_usuario, saldo_usuario)
    print(texto)


def formatar_com_format_por_posicao(nome_usuario: str, idade_usuario: int, saldo_usuario: float):
    texto = "Bem vindo {}! Sua idade é {} você tem o saldo de {}".format(nome_usuario,idade_usuario,saldo_usuario)
    print(texto)


def formatar_com_format_nomeado(nome_usuario: str, idade_usuario: int, saldo_usuario: float):
    texto = "Bem vindo {nome}! Sua idade é {idade} você tem o saldo de {saldo}".format(
        nome=nome_usuario, idade=idade_usuario, saldo=saldo_usuario,
        )
    print(texto)


def formatar_com_format_top(nome_usuario: str, idade_usuario: int, saldo_usuario: float):
    texto = f"Bem vindo {nome_usuario}! Sua idade é {idade_usuario} você tem o saldo de {saldo_usuario:.2f}"
    print(texto)


os.system("cls")
formatar_com_percentual("Gustavo", 19, 1395.20)
formatar_com_format_por_posicao("Aniela", 37, 560912.00)
formatar_com_format_nomeado("Pedro", 1, 340897.10)
formatar_com_format_top("Thanos", 470, 0.05)