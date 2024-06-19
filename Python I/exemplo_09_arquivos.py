import os
# Modo de Leitura e Escrita de arquivos
# arquivo = open("nomeArquivo.txt", "r") # read, abre o arquivo em modo de leitura, o arquivo deve existir
# arquivo = open("nomeArquivo.txt", "w") # write, abre o arquivo em modo de escrita, 
#                                          cria o arquivo caso não existir, caso existir remove o conteúdo
# arquivo = open("nomeArquivo.txt", "a") # append, abre o arquivo em modo de escrita, cria o arquivo caso não existir.
#                                        Irá adicionar o conteúdo quando chamado o write, ou seja, esse modo não irá 
#                                        apagar o conteúdo anterior
# arquivo = open("nomeArquivo.txt", "r+") # read, write, abre o arquivo em modo de leitura/escrita, o arquivo deve existir
# arquivo = open("nomeArquivo.txt", "w+") # read, write, abre o arquivo em modo de leitura/escrita,
#                                          cria o arquivo caso não existir, caso existir remove o conteúdo
# arquivo = open("nomeArquivo.txt", "a+") # read, append, abre o arquivo em modo de leitura/adição,
#                                          cria o arquivo caso não existir.
#                                          Irá adicionar o conteúdo quando chamado o write, ou seja, esse modo não irá 
#                                          apagar o conteúdo anterior

def exemplo_verificar_arquivo_existe():
    arquivo_existe = os.path.exists("texto.txt")
    if arquivo_existe == True:
        print("Arquivo 'texto.txt' existe")
    else:
        print("Arquivo 'texto.txt' não existe")


def exemplo_apagar_arquivo():
    # Verificar se o aquivo existe
    if os.path.exists("texto.txt") == True:
        # Apagar o arquivo da máquina do usuário
        os.remove("texto.txt")
        print("Removido arquivo 'texto.txt'")
    else:
        print("Arquivo 'texto.txt' não existe")


def exemplo_criar_arquivo() -> str:
    # Abrir o arquivo e limpar o conteúdo
    arquivo = open("texto.txt", "w")
    # Escrever no arquivo
    arquivo.write("Hello World2")
    # Fechar o arquivo aberto
    arquivo.close()


def exemplo_ler_arquivo() -> str:
    # Abrir o arquivo no modo de leitura
    arquivo = open("texto.txt", "r")
    # Obter todas as linhas do arquivo
    linhas = arquivo.readlines()
    # Fechar o arquivo
    arquivo.close()
    # Percorrer cada uma das linhas
    for i in range(len(linhas)):
        linha = linhas[i]
        print(linha, end="")


def exemplo_acrescentar_texto_no_aquivo():
    arquivo = open("texto.txt", "a")
    arquivo.write("\nMinha segunda linha")
    arquivo.close()




exemplo_apagar_arquivo()
exemplo_criar_arquivo()
exemplo_acrescentar_texto_no_aquivo()
exemplo_ler_arquivo()
exemplo_apagar_arquivo()
