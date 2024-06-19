from typing import Any, Dict, List
import mysql.connector


def conectar():
    # Criando a conexão com o servidor do mysql
    conexao = mysql.connector.connect(
    host="127.0.0.1", # Localhost ou 127.0.0.1 é a sua máquina
    port=3306,
    user="root",
    password="admin",
    )
    return conexao


def setup():
    #apagar_banco_dados()
    if verificar_banco_dados_existe() == False:
        criar_banco_dados()
        criar_tabelas()
        popular_registros()


def criar_tabelas():
    criar_tabela_categarias()
    criar_tabela_carros()
    criar_tabela_marcas()
    criar_tabela_clientes()
    criar_tabela_produtos()
    criar_tabela_contatos()


def popular_registros():
    popular_registros_tabela_categorias()
    popular_registros_tabela_carros()
    popular_registros_tabela_marcas()
    popular_registros_tabela_clientes()
    popular_registro_tabela_produtos()
    popular_registros_tabela_contatos()


def popular_registros_tabela_categorias():
    inserir_registro_tabela_categorias("Hatch")
    inserir_registro_tabela_categorias("Sedan")
    inserir_registro_tabela_categorias("Pickup")


def popular_registros_tabela_carros():
    inserir_registro_tabela_carros("Gol Quadrado")
    inserir_registro_tabela_carros("Polo")
    inserir_registro_tabela_carros("Mustang")


def popular_registros_tabela_marcas():
    inserir_registro_tabela_marcas("Volvo" , "SC - Blumenau - Rua São Paula - 1700")
    inserir_registro_tabela_marcas("Volkswagen", "SC - Joinville - Rua Vila Nova - 1320")
    inserir_registro_tabela_marcas("Ford", "SC - Florianopolis - Rua Sete de Setembro - 580")


def popular_registros_tabela_clientes():
    inserir_registro_tabela_clientes("João", "554.649.584-52")
    inserir_registro_tabela_clientes("Andrey", "754.259.168-24")
    inserir_registro_tabela_clientes("Jessica", "854.369.642-30")


def verificar_banco_dados_existe() -> bool:
    conexao = conectar()
    # Criando cursor que permitirá executar comandos do mysql
    cursor = conexao.cursor()
    # Consultar na tabela onde contém os dados dos bancos de dados, verificando se existe o banco de dados com nome loja_db
    cursor.execute("SELECT SCHEMA_NAME FROM INFORMATION_SCHEMA.SCHEMATA WHERE SCHEMA_NAME = 'loja_db'")
    # Obter um registro da consulta
    resultado = cursor.fetchone()
    # Verificar que a consulta retornou um registro, ou seja, o banco de dados existe com o nome 'loja_db'
    if resultado is not None:
        # Desta forma, retornando true, pois o banco de dados existe
        return True
    else:
        return False


def apagar_banco_dados():
    # print("Criando banco de dados loja_db")
    conexao = conectar()
    # Criando cursor que permitirá executar comandos no mysql
    cursor = conexao.cursor()
    # cursor.execute("DROP DATABASE IF EXISTS loja_db")
    cursor.execute("DROP DATABASE IF EXISTS loja_db")
    conexao.commit()
    conexao.close()
    # SHOW SCHEMAS;
    # print("Banco de dados criado com sucesso")


def criar_banco_dados():
    # print("Criando banco de dados loja_db")
    conexao = conectar()
    # Criando cursor que permitirá executar comandos no mysql
    cursor = conexao.cursor()
    # cursor.execute("DROP DATABASE IF EXISTS loja_db")
    cursor.execute("CREATE DATABASE loja_db")
    conexao.commit()
    conexao.close()
    # SHOW SCHEMAS;
    # print("Banco de dados criado com sucesso")


def definir_banco_dados(cursor):
    #print("Definindo banco dados loja_db")
    cursor.execute("USE loja_db")
    #print("Definido banco de dados")
    return cursor


def criar_tabela_categarias():
    # print("Criando tabela categorias")
    conexao = conectar()
    # Criando cursor que permitirá executar comandos no mysql
    cursor = conexao.cursor()
    cursor = definir_banco_dados(cursor) # Definir o banco de dados que será utilizado, ou seja, USE loja_db
    cursor.execute("""
                    CREATE TABLE categorias (
                        id INT PRIMARY KEY AUTO_INCREMENT,
                        nome VARCHAR(100) NOT NULL
                    )
                    """)
    conexao.commit()
    conexao.close()
    # print("Tabela categorias criada com sucesso")


def criar_tabela_carros():
    # print("Criando tabela carros")
    conexao = conectar()
    cursor = conexao.cursor()
    cursor = definir_banco_dados(cursor)
    cursor.execute("""
                    CREATE TABLE carros (
                        id INT PRIMARY KEY AUTO_INCREMENT,
                        nome VARCHAR(100) NOT NULL
                    )
                    """)
    conexao.commit()
    conexao.close()
    # print("Tabela carros criada com sucesso")


def criar_tabela_marcas():
    # print("Criando tabela marcas")
    conexao = conectar()
    cursor = conexao.cursor()
    cursor = definir_banco_dados(cursor)
    cursor.execute(""" 
                    CREATE TABLE marcas (
                    id INT PRIMARY KEY AUTO_INCREMENT,
                    nome VARCHAR(50) NOT NULL,
                    endereco VARCHAR(150) NOT NULL
                    )
                    """)
    conexao.commit()
    conexao.close()
    # print("Tabela marcas criada com sucesso")


def criar_tabela_clientes():
    # print("Criando tabela clientes")
    conexao = conectar()
    cursor = conexao.cursor()
    cursor = definir_banco_dados(cursor)
    cursor.execute("""
                    CREATE TABLE clientes(
                    id INT PRIMARY KEY AUTO_INCREMENT,
                    nome VARCHAR(50) NOT NULL,
                    cpf VARCHAR(14) NOT NULL
                    )
                    """)
    conexao.commit()
    conexao.close()
    # print("Tabela clientes criada com sucesso")


def inserir_registro_tabela_categorias(nome: str):
    # print("Criando registro na tabela de categorias")
    conexao = conectar()
    # Criando cursor que permitirá executar comandos no mysql
    cursor = conexao.cursor()
    cursor = definir_banco_dados(cursor) # Definir o banco de dados que será utilizado, ou seja, USE loja_db
    cursor.execute("INSERT INTO categorias (nome) VALUES (%s);", (nome,))
    conexao.commit()
    conexao.close()
    # print("Registro criando com sucesso")


def inserir_registro_tabela_carros(nome: str):
    # print("Criando registro na tabela de carros")
    conexao = conectar()
    # Criando cursor que permitirá executar comandos no mysql
    cursor = conexao.cursor()
    cursor = definir_banco_dados(cursor) # Definir o banco de dados que será utilizado, ou seja, USE loja_db
    cursor.execute("INSERT INTO carros (nome) VALUES (%s)", (nome,))
    conexao.commit()
    conexao.close()
    # print("Registro criando com sucesso")


def inserir_registro_tabela_marcas(nome: str, endereco: str):
    # print("Criando registro na tabela de marcas")
    conexao = conectar()
    # Criando cursor que permitirá executar comandos no mysql
    cursor = conexao.cursor()
    cursor = definir_banco_dados(cursor) # Definir o banco de dados que será utilizado, ou seja, USE loja_db
    cursor.execute("INSERT INTO marcas (nome, endereco) VALUES (%s, %s)", (nome, endereco))
    conexao.commit()
    conexao.close()
    # print("Registro criando com sucesso")


def inserir_registro_tabela_clientes(nome: str, cpf: str):
    # print("Criando registro na tabela de clientes")
    conexao = conectar()
    # Criando cursor que permitirá executar comandos no mysql
    cursor = conexao.cursor()
    cursor = definir_banco_dados(cursor) # Definir o banco de dados que será utilizado, ou seja, USE loja_db
    cursor.execute("INSERT INTO clientes (nome, cpf) VALUES (%s, %s)", (nome, cpf))
    conexao.commit()
    conexao.close()
    # print("Registro criando com sucesso")


def consultar_registro_tabela_categorias():
    # print("Consultar registros da tabela de categorias")
    conexao = conectar()
    # Criando cursor que permitirá executar comandos no mysql
    cursor = conexao.cursor()
    cursor = definir_banco_dados(cursor)# Definir o banco de dados que será utilizado, ou seja, USE loja_db
    cursor.execute("SELECT id, nome FROM categorias")
    # Executar a consulta do SELECT buscando todas as categorias
    registros = cursor.fetchall()
    conexao.close()
    #Criar a lista de categorias vazia
    categorias = []
    # Percorrer cada um dos registros do banco de dados
    for registro in registros:
        # Gerar o dicionário (chave, valor) com os dados do registro
        categoria = {
            "id": registro[0],
            "nome": registro[1]
        }
        # Adicionar o dicionário(dados da categoria) na lista de categorias
        categorias.append(categoria)
    # A lista de categorias (que contém uma lista de dicionários com os dados das categorias)
    return categorias


def consultar_registro_tabela_carros():
    # print("Consultar registros da tabela de carros")
    conexao = conectar()
    # Criando cursor que permitirá executar comandos no mysql
    cursor = conexao.cursor()
    cursor = definir_banco_dados(cursor)# Definir o banco de dados que será utilizado, ou seja, USE loja_db
    cursor.execute("SELECT id, nome FROM carros")
    # Executar a consulta do SELECT buscando todas as categorias
    registros = cursor.fetchall()
    conexao.close()
    #Criar a lista de carros vazia
    carros = []
    # Percorrer cada um dos registros do banco de dados
    for registro in registros:
        # Gerar o dicionário (chave, valor) com os dados do registro
        carro = {
            "id": registro[0],
            "nome": registro[1]
        }
        # Adicionar o dicionário(dados da categoria) na lista de categorias
        carros.append(carro)
    # A lista de categorias (que contém uma lista de dicionários com os dados das categorias)
    return carros


def consultar_registro_tabela_marcas():
    # print("Consultar registros da tabela de marcas")
    conexao = conectar()
    # Criando cursor que permitirá executar comandos no mysql
    cursor = conexao.cursor()
    cursor = definir_banco_dados(cursor)# Definir o banco de dados que será utilizado, ou seja, USE loja_db
    cursor.execute("SELECT id, nome, endereco FROM marcas")
    # Executar a consulta do SELECT buscando todas as marcas
    registros = cursor.fetchall()
    conexao.close()
    #Criar a lista de marcas vazia
    marcas = []
    # Percorrer cada um dos registros do banco de dados
    for registro in registros:
        # Gerar o dicionário (chave, valor) com os dados do registro
        marca = {
            "id": registro[0],
            "nome": registro[1],
            "endereco" : registro[2]
        }
        # Adicionar o dicionário(dados da categoria) na lista de categorias
        marcas.append(marca)
    # A lista de categorias (que contém uma lista de dicionários com os dados das categorias)
    return marcas


def consultar_registro_tabela_clientes():
    # print("Consultar registros da tabela de clientes")
    conexao = conectar()
    # Criando cursor que permitirá executar comandos no mysql
    cursor = conexao.cursor()
    cursor = definir_banco_dados(cursor)# Definir o banco de dados que será utilizado, ou seja, USE loja_db
    cursor.execute("SELECT id, nome, cpf FROM clientes")
    # Executar a consulta do SELECT buscando todas os clientes
    registros = cursor.fetchall()
    conexao.close()
    #Criar a lista de clientes vazio
    clientes = []
    # Percorrer cada um dos registros do banco de dados
    for registro in registros:
        # Gerar o dicionário (chave, valor) com os dados do registro
        cliente = {
            "id": registro[0],
            "nome": registro[1],
            "cpf" : registro[2]
        }
        # Adicionar o dicionário(dados da categoria) na lista de categorias
        clientes.append(cliente)
    # A lista de categorias (que contém uma lista de dicionários com os dados das categorias)
    return clientes


def alterar_registro_tabela_categorias(id: int, nome: str):
    # Abre a conexão com o banco de dados
    conexao = conectar()
    cursor = conexao.cursor()
    # Definir o banco de dados
    cursor = definir_banco_dados(cursor)
    # Definir a query que será executada
    cursor.execute("UPDATE categorias SET nome = %s WHERE id = %s", (nome, id))
    # Efetivar a atualização na base de dados
    conexao.commit()
    # Fechar conexão com a base de dados
    conexao.close()


def alterar_registro_tabela_carros(id: int, nome: str):
    # Abre a conexão com o banco de dados
    conexao = conectar()
    cursor = conexao.cursor()
    # Definir o banco de dados
    cursor = definir_banco_dados(cursor)
    # Definir a query que será executada
    cursor.execute("UPDATE carros SET nome = %s WHERE id = %s", (nome, id))
    # Efetivar a atualização na base de dados
    conexao.commit()
    # Fechar conexão com a base de dados
    conexao.close()


def alterar_registro_tabela_marcas(id: int, nome: str, endereco: str):
    # Abre a conexão com o banco de dados
    conexao = conectar()
    cursor = conexao.cursor()
    # Definir o banco de dados
    cursor = definir_banco_dados(cursor)
    # Definir a query que será executada
    cursor.execute("UPDATE marcas SET nome = %s, endereco = %s WHERE id = %s", (nome, endereco, id))
    # Efetivar a atualização na base de dados
    conexao.commit()
    # Fechar conexão com a base de dados
    conexao.close()


def alterar_registro_tabela_clientes(id: int, nome: str, cpf: str):
    # Abre a conexão com o banco de dados
    conexao = conectar()
    cursor = conexao.cursor()
    # Definir o banco de dados
    cursor = definir_banco_dados(cursor)
    # Definir a query que será executada
    cursor.execute("UPDATE clientes SET nome = %s, cpf = %s WHERE id = %s", (nome, cpf, id))
    # Efetivar a atualização na base de dados
    conexao.commit()
    # Fechar conexão com a base de dados
    conexao.close()


def apagar_registro_tabela_categorias(id: int):
    # print("Apagando registro da tabela de categorias")
    conexao = conectar()
    cursor = conexao.cursor()
    cursor = definir_banco_dados(cursor)
    cursor.execute("DELETE FROM categorias WHERE id = %s", (id,))
    conexao.commit()
    conexao.close()


def apagar_registro_tabela_carros(id: int):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor = definir_banco_dados(cursor)
    cursor.execute("DELETE FROM carros WHERE id = %s", (id,))
    conexao.commit()
    conexao.close()


def apagar_registro_tabela_marcas(id: int):
    # print("Apagando registro da tabela de marcas")
    conexao = conectar()
    cursor = conexao.cursor()
    cursor = definir_banco_dados(cursor)
    cursor.execute("DELETE FROM marcas WHERE id = %s", (id,))
    conexao.commit()
    conexao.close()


def apagar_registro_tabela_clientes(id: int):
    # print("Apagando registro da tabela de clientes")
    conexao = conectar()
    cursor = conexao.cursor()
    cursor = definir_banco_dados(cursor)
    cursor.execute("DELETE FROM clientes WHERE id = %s", (id,))
    conexao.commit()
    conexao.close()



def criar_tabela_produtos():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor = definir_banco_dados(cursor)
    cursor.execute("""
        CREATE TABLE produtos(
            id INT PRIMARY KEY AUTO_INCREMENT,
            nome VARCHAR(100),
            id_categoria INT, -- FK referenciar uma pk de outra tabela
            FOREIGN KEY (id_categoria) REFERENCES categorias(id) -- Chave estrangeira
        );""")
    conexao.commit()
    conexao.close()


def popular_registro_tabela_produtos():
    inserir_registro_tabela_produtos("HB20 Evolution", 1)
    inserir_registro_tabela_produtos("Celta", 1)
    inserir_registro_tabela_produtos("Onix", 2)
    inserir_registro_tabela_produtos("Ranger", 3)
    inserir_registro_tabela_produtos("S10", 3)


def inserir_registro_tabela_produtos(nome: str, id_categoria: int):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor = definir_banco_dados(cursor)
    cursor.execute("INSERT INTO produtos (nome, id_categoria) VALUES (%s, %s)", (nome, id_categoria))
    conexao.commit()
    conexao.close()


def consultar_registro_tabela_produtos() -> List[Dict[str, Any]]:
    conexao = conectar()
    cursor = conexao.cursor()
    cursor = definir_banco_dados(cursor)
    cursor.execute("""
        SELECT
            produtos.id,
            produtos.nome,
            produtos.id_categoria,
            categorias.nome
        FROM produtos
        INNER JOIN categorias ON (produtos.id_categoria = categorias.id)
    """)
    registros = cursor.fetchall()
    produtos = []
    for registro in registros:
        produto = {
            "id": registro[0],
            "nome": registro[1],
            "categoria": {
                "id": registro[2],
                "nome": registro[3],
            }
        }
        produtos.append(produto)
    return produtos


def apagar_registro_tabela_produtos(id: int):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor = definir_banco_dados(cursor)
    cursor.execute("DELETE FROM produtos WHERE id = %s", (id,))
    conexao.commit()
    conexao.close()


def alterar_registro_tabela_produtos(produto: Dict[str, Any]):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor = definir_banco_dados(cursor)
    cursor.execute(
        "UPDATE produtos SET nome = %s, id_categoria = %s WHERE id = %s",
        (produto.get("nome"), produto.get("categoria").get("id"), produto.get("id"))
    )
    conexao.commit()
    conexao.close

# CRUD (Create, Read, Update, Delete)



# Exercício de tabelas relacionadas
""" Criar uma tabela de contatos que permitirá adicionar contatos para os clientes registrados
- database_operacoes.py criar def criar_tabela_contatos para criar a tabela de contatos com os seguintes campos:
  - id PK
  - id_cliente FK 
  - tipo VARCHAR(10) (E-mail, Celular, Telefone, Insta)
  - valor VARCHAR(100)
- database_operacoes.py criar def popular_registros_tabela_contatos, registrando 2 contatos para o primeiro cliente e 1 para outro cliente
- database_operacoes.py criar def consultar_registros_tabela_contatos, que fará o select na tabela de contatos com inner join da tabela de clientes, construir uma lista de dicionários com os clientes da consulta (registros)
- index.py adicionar menu de CRUD do contato
- index.py criar def listar_todos_contatos, apresentar tabela com os registros retornados da função consultar_registros_tabela_contatos """


def criar_tabela_contatos():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor = definir_banco_dados(cursor)
    cursor.execute("""
                   CREATE TABLE contatos(
                   id INT PRIMARY KEY AUTO_INCREMENT,
                   id_clientes INT, FOREIGN KEY (id_clientes) REFERENCES clientes(id),
                   tipo VARCHAR(10),
                   valor VARCHAR(100)
                    );""")
    conexao.commit()
    conexao.close()


def popular_registros_tabela_contatos():
    inserir_registro_tabela_contatos(1, "E-mail", "joao@gmai.com")
    inserir_registro_tabela_contatos(1, "Celular", "(47) 99958-6524")
    inserir_registro_tabela_contatos(2, "E-mail", "andrey@gmail.com")


def inserir_registro_tabela_contatos(id_clientes: int, tipo: str, valor: str):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor = definir_banco_dados(cursor)
    cursor.execute("INSERT INTO contatos (id_clientes, tipo, valor) VALUES (%s, %s, %s)", (id_clientes, tipo, valor))
    conexao.commit()
    conexao.close()


def consultar_registro_tabela_contatos():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor = definir_banco_dados(cursor)
    cursor.execute("""
        SELECT
            contatos.id,
            contatos.id_clientes,
            clientes.nome,
            contatos.tipo,
            contatos.valor
        FROM contatos
        INNER JOIN clientes ON(contatos.id_clientes = clientes.id)    
    """)
    registros = cursor.fetchall()
    contatos = []
    for registro in registros:
        contato = {
            "id": registro[0],
            "clientes": {
                "id": registro[1],
                "nome": registro[2],
            },
            "tipo": registro[3],
            "valor": registro[4],
        }
        contatos.append(contato)
    return contatos


def apagar_registro_tabela_contatos(id: int):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor = definir_banco_dados(cursor)
    cursor.execute("DELETE FROM contatos WHERE id = %s", (id,))
    conexao.commit()
    conexao.close()


def alterar_registro_tabela_contatos(contato: Dict[str, Any]):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor = definir_banco_dados(cursor)
    cursor.execute(
        "UPDATE contatos SET tipo = %s, valor = %s WHERE id = %s",
        (contato.get("tipo"), contato.get("valor"), contato.get("id"))
    )
    conexao.commit()
    conexao.close()