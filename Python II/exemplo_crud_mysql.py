import os

from database_operacoes import consultar_registro_tabela_carros, consultar_registro_tabela_categorias, consultar_registro_tabela_clientes, consultar_registro_tabela_marcas, criando_tabela_carros, criando_tabela_clientes, criando_tabela_marcas, criar_banco_dados, criar_tabela_categarias, inserindo_registro_tabela_carros, inserindo_registro_tabela_categorias, inserindo_registro_tabela_clientes, inserindo_registro_tabela_marcas


os.system("cls")
criar_banco_dados()
criar_tabela_categarias()
criando_tabela_carros()
criando_tabela_marcas()
criando_tabela_clientes()
inserindo_registro_tabela_categorias("Hatch")
inserindo_registro_tabela_categorias("Sedan")
inserindo_registro_tabela_carros("Gol Quadrado")
inserindo_registro_tabela_marcas("Fiat", "SC - Blumenau - Rua São Paula - 1700")
inserindo_registro_tabela_clientes("João", "554.649.584-52")
consultar_registro_tabela_categorias()
consultar_registro_tabela_carros()
consultar_registro_tabela_marcas()
consultar_registro_tabela_clientes()