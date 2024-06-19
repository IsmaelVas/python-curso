import os
from typing import Any, Dict, List, Optional
import questionary
from rich.table import Table
from rich.console import Console

from database_operacoes import alterar_registro_tabela_carros, alterar_registro_tabela_categorias, alterar_registro_tabela_clientes, alterar_registro_tabela_contatos, alterar_registro_tabela_marcas, alterar_registro_tabela_produtos, apagar_registro_tabela_carros, apagar_registro_tabela_categorias, apagar_registro_tabela_clientes, apagar_registro_tabela_contatos, apagar_registro_tabela_marcas, apagar_registro_tabela_produtos, consultar_registro_tabela_carros, consultar_registro_tabela_categorias, consultar_registro_tabela_clientes, consultar_registro_tabela_contatos, consultar_registro_tabela_marcas, consultar_registro_tabela_produtos, inserir_registro_tabela_carros, inserir_registro_tabela_categorias, inserir_registro_tabela_clientes, inserir_registro_tabela_contatos, inserir_registro_tabela_marcas, setup

os.system("cls")


def listar_todos_categorias():
    categorias = consultar_registro_tabela_categorias()
    # Verificar se a lista de categorias é vazia
    if len(categorias) == 0:
        # Apresentar mensagem de que não existe categoria cadastrada
        print("Nenhuma categoria cadastrada")
        # return encerrar a execução da função listar_todos, ou seja, não apresentará a tabela
        return
    tabela = Table()
    tabela.add_column("Código")
    tabela.add_column("Nome")

    for categoria in categorias:
        tabela.add_row(str(categoria.get("id")), categoria.get("nome"))

    console = Console()
    console.print(tabela)


def listar_todos_carros():
    carros = consultar_registro_tabela_carros()
    if len(carros) == 0:
        print("Nenhum carro cadastrado")
        return
    tabela = Table()
    tabela.add_column("Código")
    tabela.add_column("Nome")

    for carro in carros:
        tabela.add_row(str(carro.get("id")), carro.get("nome"))

    conselo = Console()
    conselo.print(tabela)


def listar_todos_marcas():
    marcas = consultar_registro_tabela_marcas()
    if len(marcas) == 0:
        print("Nenhum marca cadastrado")
        return
    tabela = Table()
    tabela.add_column("Código")
    tabela.add_column("Nome")
    tabela.add_column("Endereço")

    for marca in marcas:
        tabela.add_row(str(marca.get("id")), marca.get("nome"), marca.get("endereco"))

    conselo = Console()
    conselo.print(tabela)


def listar_todos_clientes():
    clientes = consultar_registro_tabela_clientes()
    if len(clientes) == 0:
        print("Nenhum cliente cadastrado")
        return
    tabela = Table()
    tabela.add_column("Código")
    tabela.add_column("Nome")
    tabela.add_column("CPF")

    for cliente in clientes:
        tabela.add_row(str(cliente.get("id")), cliente.get("nome"), cliente.get("cpf"))

    conselo = Console()
    conselo.print(tabela)


def listar_todos_produtos():
    produtos = consultar_registro_tabela_produtos()
    if len(produtos) == 0:
        print("Nenhum produto cadastrado")
        return
    tabela = Table()
    tabela.add_column("Código")
    tabela.add_column("Categoria")
    tabela.add_column("Nome")

    for produto in produtos:
        tabela.add_row(str(produto.get("id")), produto.get("categoria").get("nome"), produto.get("nome"))

    console = Console()
    console.print(tabela)


def listar_todos_contatos():
    contatos = consultar_registro_tabela_contatos()
    if len(contatos) == 0:
        print("Nenhum contato cadastrado")
        return
    tabela = Table()
    tabela.add_column("Código")
    tabela.add_column("Nome")
    tabela.add_column("Tipo de contato")
    tabela.add_column("Contato")



    for contato in contatos:
        tabela.add_row(str(contato.get("id")), contato.get("clientes").get("nome"), contato.get("tipo"), contato.get("valor"))

    console = Console()
    console.print(tabela)


def cadastrar_categorias():
    nome = questionary.text("Digite o nome da categoria: ").ask().strip()
    inserir_registro_tabela_categorias(nome)


def cadastrar_carros():
    nome = questionary.text("Digite o nome da carros: ").ask().strip()
    inserir_registro_tabela_carros(nome)


def cadastrar_marcas():
    nome = questionary.text("Digite o nome da marcas: ").ask().strip()
    endereco = questionary.text("Digite o endereço: ").ask().strip()
    inserir_registro_tabela_marcas(nome, endereco)


def cadastrar_clientes():
    nome = questionary.text("Digite o nome do cliente: ").ask().strip()
    cpf = questionary.text("Digite o CPF do cliente: ").ask().strip()

    inserir_registro_tabela_clientes(nome, cpf)


def obter_categorias_choices() -> List[questionary.Choice]:
    # Obter a lista de categorias para permitir o usuário escolher a categoria
    # Que o produto será atrelado
    categorias = consultar_registro_tabela_categorias()
    categorias_choices = []
    for categoria in categorias:
        categorias_choices.append(questionary.Choice(categoria.get("nome"), categoria))
    return categorias_choices


def cadastrar_produtos():
    categorias_choices = obter_categorias_choices()
    nome = questionary.text("Digite o nome do produto: ").ask().strip()
    categoria = questionary.select("Escolha a categoria: ", categorias_choices).ask()

    inserir_registro_tabela_clientes(nome, categoria.get("id"))
    print("Produtos cadastrado com sucesso")


def obter_clientes_choices() -> List[questionary.Choice]:
    clientes = consultar_registro_tabela_clientes()
    clientes_choices = []
    for cliente in clientes:
        clientes_choices.append(questionary.Choice(cliente.get("nome"), cliente))
    return clientes_choices


def cadastrar_contatos():
    clientes_choices = obter_clientes_choices()
    cliente = questionary.select("Escolha o cliente para cadastrar o contato: ", clientes_choices).ask()

    tipo = questionary.select("Escolha um contato:", ["E-mail", "Celular", "Telefone", "Instagram"]).ask()
    valor = questionary.text("Digite o contato: ").ask().strip()

    inserir_registro_tabela_contatos(cliente.get("id"), tipo, valor)
    print("Contato cadastrado com sucesso")


def editar_categorias():
        # Consultar as categorias do banco de dados
    categorias = consultar_registro_tabela_categorias()
    # Verificando se não existe categorias cadastradas
    if len(categorias) == 0:
        print("Nenhuma categotia cadastrada, não sendo possível editar neste momento.")
        # Encerre a exccução da função editar, ou seja, não irá apresentar a opção para escolher
        return
    # Criar uma lista de choice para o usuário poder escolher utilizado o questionary
    categorias_choices = []
    for categoria in categorias:
        categorias_choices.append(questionary.Choice(categoria.get("nome"), categoria))
    # Perguntar para o usuário qual a categoria que ele desejar editar
    categoria_escolhida = questionary.select("Escolha a categoria para editar:", categorias_choices).ask()
    categoria_escolhida["nome"] = questionary.text(
        "Edite o nome da categoria: ",
        categoria_escolhida.get("nome")
        ).ask().strip()
    # Chamar a função que executará o update na tabela de categorias, para efetivar a atualização na base de dados
    alterar_registro_tabela_categorias(categoria_escolhida.get("id"), categoria_escolhida.get("nome"))


def editar_carros():
    # Consultar as carros do banco de dados
    carros = consultar_registro_tabela_carros()
    # Verificando se não existe carros cadastrados
    if len(carros) == 0:
        print("Nenhum carro cadastrado, não sendo possível editar neste momento.")
        # Encerre a exccução da função editar, ou seja, não irá apresentar a opção para escolher
        return
    # Criar uma lista de choice para o usuário poder escolher utilizado o questionary
    carros_choices = []
    for carro in carros:
        carros_choices.append(questionary.Choice(carro.get("nome"), carro))
    # Perguntar para o usuário qual o carro que ele desejar editar
    carro_escolhido = questionary.select("Escolha o carro para editar:", carros_choices).ask()
    carro_escolhido["nome"] = questionary.text(
        "Edite o nome do carro: ",
        carro_escolhido.get("nome")
        ).ask().strip()
    # Chamar a função que executará o update na tabela de carros, para efetivar a atualização na base de dados
    alterar_registro_tabela_carros(carro_escolhido.get("id"), carro_escolhido.get("nome"))


def editar_marcas():
    # Consultar as marcas do banco de dados
    marcas = consultar_registro_tabela_marcas()
    # Verificando se não existe marcas cadastradas
    if len(marcas) == 0:
        print("Nenhuma marca cadastrada, não sendo possível editar neste momento.")
        # Encerre a exccução da função editar, ou seja, não irá apresentar a opção para escolher
        return
    # Criar uma lista de choice para o usuário poder escolher utilizado o questionary
    marcas_choices = []
    for marca in marcas:
        marcas_choices.append(questionary.Choice(marca.get("nome"), marca))
        marcas_choices.append(questionary.Choice(marca.get("endereco"), marca))
    # Perguntar para o usuário qual a marca que ele desejar editar
    marca_escolhida = questionary.select("Escolha a marca para editar:", marcas_choices).ask()
    marca_escolhida["nome"] = questionary.text(
        "Edite o nome da marca: ",
        marca_escolhida.get("nome")
        ).ask().strip()
    marca_escolhida["endereco"] = questionary.text(
        "Edite o enderço da marca: ",
        marca_escolhida.get("endereco")
        ).ask().strip()
    # Chamar a função que executará o update na tabela de marcas, para efetivar a atualização na base de dados
    alterar_registro_tabela_marcas(marca_escolhida.get("id"), marca_escolhida.get("nome"), marca_escolhida.get("endereco"))


def editar_clientes():
        # Consultar as categorias do banco de dados
    clientes = consultar_registro_tabela_clientes()
    # Verificando se não existe clientes cadastrados
    if len(clientes) == 0:
        print("Nenhuma cliente cadastrado, não sendo possível editar neste momento.")
        # Encerre a exccução da função editar, ou seja, não irá apresentar a opção para escolher
        return
    # Criar uma lista de choice para o usuário poder escolher utilizado o questionary
    clientes_choices = []
    for cliente in clientes:
        clientes_choices.append(questionary.Choice(clientes.get("nome"), cliente))
    # Perguntar para o usuário qual a cliente que ele desejar editar
    clientes_escolhido = questionary.select("Escolha o cliente para editar:", clientes_choices).ask()
    clientes_escolhido["nome"] = questionary.text(
        "Edite o nome do cliente: ",
        clientes_escolhido.get("nome")
        ).ask().strip()
    clientes_escolhido["cpf"] = questionary.text(
        "Edite o CPF do cliente: ",
        clientes_escolhido.get("cpf")
        ).ask().strip()        
    # Chamar a função que executará o update na tabela de clientes, para efetivar a atualização na base de dados
    alterar_registro_tabela_clientes(clientes_escolhido.get("id"), clientes_escolhido.get("nome"), clientes_escolhido.get("cpf"))


def editar_produtos():
    produto_escolhido = escolher_produto()
    if produto_escolhido is None:
        return
    
    categorias_choices = obter_categorias_choices()
    produto_escolhido["nome"] = questionary.text(
        "Digite o nome do produto: ", default=produto_escolhido.get("nome"),
    ).ask().strip()
    produto_escolhido["categoria"] = questionary.select(
        "Escolha a categoria: ", categorias_choices, default=produto_escolhido.get("categoria"),
    ).ask()
    alterar_registro_tabela_produtos(produto_escolhido)
    print("Produto alterado com sucesso")


def editar_contatos():
    contato_escolhido = escolher_contato()
    if contato_escolhido is None:
        return
    
    contato_escolhido["tipo"] = questionary.select(
        "Alterar o tipo: \n Escolha o tipo de contato: ", ["E-mail", "Celular", "Telefone", "Instagram"],
    ).ask()
    contato_escolhido["valor"] = questionary.text(
        "Digite o contato do cliente: ", default=contato_escolhido.get("valor"),
    ).ask().strip()

    alterar_registro_tabela_contatos(contato_escolhido)
    print("Contato alterado com sucesso")


def apagar_categorias():
    # Consultar as categorias do banco de dados
    categorias = consultar_registro_tabela_categorias()
    # Verificando se não existe categorias cadastradas
    if len(categorias) == 0:
        print("Nenhuma categotia cadastrada, não sendo possível apagar neste momento.")
        # Encerre a exccução da função apagar, ou seja, não irá apresentar a opção para escolher
        return
    # Criar uma lista de choice para o usuário poder escolher utilizado o questionary
    categorias_choices = []
    for categoria in categorias:
        categorias_choices.append(questionary.Choice(categoria.get("nome"), categoria.get("id")))
    # Perguntar para o usuário qual a categoria que ele desejar apagar
    id_escolhido = questionary.select("Escolha a categoria para apagar:", categorias_choices).ask()
    # Executar o delete na tabela de categorias com o id da categoria escolhida
    apagar_registro_tabela_categorias(id_escolhido)
    print("Registro apagado com sucesso")


def apagar_carros():
    # Consultar as carros do banco de dados
    carros = consultar_registro_tabela_carros()
    # Verificando se não existe carros cadastrados
    if len(carros) == 0:
        print("Nenhuma carro cadastrado, não sendo possível apagar neste momento.")
        # Encerre a exccução da função apagar, ou seja, não irá apresentar a opção para escolher
        return
    # Criar uma lista de choice para o usuário poder escolher utilizado o questionary
    carros_choices = []
    for carro in carros:
        carros_choices.append(questionary.Choice(carro.get("nome"), carro.get("id")))
    # Perguntar para o usuário qual a carro que ele desejar apagar
    id_escolhido = questionary.select("Escolha a carro para apagar:", carros_choices).ask()
    # Executar o delete na tabela de carros com o id da carro escolhida
    apagar_registro_tabela_carros(id_escolhido)
    print("Registro apagado com sucesso")


def apagar_marcas():
    # Consultar as marcas do banco de dados
    marcas = consultar_registro_tabela_marcas()
    # Verificando se não existe marcas cadastradas
    if len(marcas) == 0:
        print("Nenhuma marca cadastrada, não sendo possível apagar neste momento.")
        # Encerre a exccução da função apagar, ou seja, não irá apresentar a opção para escolher
        return
    # Criar uma lista de choice para o usuário poder escolher utilizado o questionary
    marcas_choices = []
    for marca in marcas:
        marcas_choices.append(questionary.Choice(marca.get("nome"), marca.get("id")))
    # Perguntar para o usuário qual a marca que ele desejar apagar
    id_escolhido = questionary.select("Escolha a marca para apagar:", marcas_choices).ask()
    # Executar o delete na tabela de marcas com o id da marca escolhida
    apagar_registro_tabela_marcas(id_escolhido)
    print("Registro apagado com sucesso")


def apagar_clientes():
    # Consultar os clientes do banco de dados
    clientes = consultar_registro_tabela_clientes()
    # Verificando se não existe clientes cadastrados
    if len(clientes) == 0:
        print("Nenhuma cliente cadastrado, não sendo possível apagar neste momento.")
        # Encerre a exccução da função apagar, ou seja, não irá apresentar a opção para escolher
        return
    # Criar uma lista de choice para o usuário poder escolher utilizado o questionary
    clientes_choices = []
    for cliente in clientes:
        clientes_choices.append(questionary.Choice(cliente.get("nome"), cliente.get("id")))
    # Perguntar para o usuário qual o cliente que ele desejar apagar
    id_escolhido = questionary.select("Escolha o cliente para apagar:", clientes_choices).ask()
    # Executar o delete na tabela de clientes com o id da cliente escolhido
    apagar_registro_tabela_clientes(id_escolhido)
    print("Registro apagado com sucesso")


def apagar_produtos():
    produto_escolhido = escolher_produto()
    if produto_escolhido is None:
        return
    confirmacao = questionary.confirm(f"Deseja realmente apagar '{produto_escolhido.get('nome')}'").ask()
    if confirmacao == False:
        return
    apagar_registro_tabela_produtos(produto_escolhido.get("id"))
    print("Produto apagado com sucesso")


def apagar_contatos():
    contato_escolhido = escolher_contato()
    if contato_escolhido is None:
        return
    confirmacao = questionary.confirm(f"Deseja realmente apagar '{contato_escolhido.get('tipo')}'").ask()
    if confirmacao == False:
        return
    apagar_registro_tabela_contatos(contato_escolhido.get("id"))
    print("Contato apagado com sucesso")


#def nomeFuncao(parametros) -> tipoRetorno
def escolher_produto() -> Optional[Dict[str, Any]]:
    produtos = consultar_registro_tabela_produtos()
    if len(produtos) == 0:
        print("Nenhum produto cadastrado")
        return None
    
    """
    choice = []
    for produto in produtos:
        choice = questionary.Choice(produto.get("nome"), produto)
        choice.append(choice)
        """
    #list comprehension
    choices = [questionary.Choice(produto.get("nome"), produto) 
               for produto in produtos]
    produto_escolhido = questionary.select("Escolha o produto", choices).ask()
    return produto_escolhido


def escolher_contato() -> Optional[Dict[str, Any]]:
    contatos = consultar_registro_tabela_contatos()
    if len(contatos) == 0:
        print("Nenhum contato cadastrado")
        return None
    
    choices = [questionary.Choice(contato.get("clientes").get("nome"), contato)
               for contato in contatos]
    contato_escolhido = questionary.select("Escolha o contato", choices).ask()
    return contato_escolhido


setup()


def menu():
    tabelas = [
        questionary.Choice("Categoria", 1),
        questionary.Choice("Carros", 2),
        questionary.Choice("Marcas", 3),
        questionary.Choice("Clientes", 4),
        questionary.Choice("Produtos", 5),
        questionary.Choice("Contatos", 6)
    ]
    continuar_tabelas = True
    while continuar_tabelas == True:
        escolha_tabela = int(questionary.select("Qual tabela deseja:", tabelas).ask())
        if escolha_tabela == 1:
            menu_categorias()
        elif escolha_tabela == 2:
            menu_carros()
        elif escolha_tabela == 3:
            menu_marcas()
        elif escolha_tabela == 4:
            menu_clientes()
        elif escolha_tabela == 5:
            menu_produtos()
        elif escolha_tabela == 6:
            menu_contatos()
        continuar_tabelas = questionary.confirm("Deseja continuar:").ask()


def menu_categorias():
    opcoes = [
        questionary.Choice("Categoria - Listar todos", 1),
        questionary.Choice("Categoria - Cadastro", 2),
        questionary.Choice("Categoria - Editar", 3),
        questionary.Choice("Categoria - Apagar", 4),
        questionary.Choice("Voltar", 1000),
    ]
    opcao = 0
    while opcao != 1000:
        opcao = int(questionary.select("Escolha o menu:", opcoes).ask())
        match(opcao):
            case 1: listar_todos_categorias(),
            case 2: cadastrar_categorias(),
            case 3: editar_categorias()
            case 4: apagar_categorias()   


def menu_carros():
    opcoes = [
        questionary.Choice("Carros - Listar todos", 1),
        questionary.Choice("Carros - Cadastro", 2),
        questionary.Choice("Carros - Editar", 3),
        questionary.Choice("Carros - Apagar", 4),
        questionary.Choice("Voltar", 1000)
    ]
    opcao = 0
    while opcao != 1000:
        opcao = int(questionary.select("Escolha o menu: ", opcoes).ask())
        match(opcao):
            case 1: listar_todos_carros(),
            case 2: cadastrar_carros(),
            case 3: editar_carros()
            case 4: apagar_carros()


def menu_marcas():
    opcoes = [
        questionary.Choice("Marcas - Listar todos", 1),
        questionary.Choice("Marcas - Editar", 3),
        questionary.Choice("Marcas - Cadastro", 2),
        questionary.Choice("Marcas - Apagar", 4),
        questionary.Choice("Voltar", 1000)
        ]
    opcao = 0
    while opcao != 1000:
        opcao = int(questionary.select("Escolha o menu: ", opcoes).ask())
        match(opcao):
            case 1: listar_todos_marcas(),
            case 2: cadastrar_marcas(),
            case 3: editar_marcas()
            case 4: apagar_marcas()


def menu_clientes():
    opcoes = [
            questionary.Choice("Clientes - Listar todos", 1),
            questionary.Choice("Clientes - Cadastro", 2),
            questionary.Choice("Clientes - Editar", 3),
            questionary.Choice("Clientes - Apagar", 4),
            questionary.Choice("Voltar", 1000)
        ]
    opcao = 0
    while opcao != 1000:
        opcao = int(questionary.select("Escolha o menu: ", opcoes).ask())
        match(opcoes):
            case 1: listar_todos_clientes(),
            case 2: cadastrar_clientes(),
            case 3: editar_clientes()
            case 4: apagar_clientes()


def menu_produtos():
    opcoes = [
            questionary.Choice("Produtos - Listar todos", 1),
            questionary.Choice("Produtos - Cadastro", 2),
            questionary.Choice("Produtos - Editar", 3),
            questionary.Choice("Produtos - Apagar", 4),
            questionary.Choice("Voltar", 1000)
        ]
    opcao = 0
    while opcao != 1000:
        opcao = int(questionary.select("Escolha o menu: ", opcoes).ask())
        match(opcao):
            case 1: listar_todos_produtos()
            case 2: cadastrar_produtos()
            case 3: editar_produtos()
            case 4: apagar_produtos()


def menu_contatos():
    opcoes = [
            questionary.Choice("Contatos - Listar todos", 1),
            questionary.Choice("Contatos - Cadastro", 2),
            questionary.Choice("Contatos - Editar", 3),
            questionary.Choice("Contatos - Apagar", 4),
            questionary.Choice("Voltar", 1000)
        ]
    opcao = 0
    while opcao != 1000:
        opcao = int(questionary.select("Escolha o menu: ", opcoes).ask())
        match(opcao):
            case 1: listar_todos_contatos()
            case 2: cadastrar_contatos()
            case 3: editar_contatos()
            case 4: apagar_contatos()


menu()