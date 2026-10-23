import json

def carregar_produtos():
    arquivo = open("produtos.json", "r", encoding="utf-8")
    produtos = json.load(arquivo)
    arquivo.close()
    return produtos

def salvar_produtos(produtos):
    arquivo = open("produtos.json", "w", encoding="utf-8")
    json.dump(produtos, arquivo, indent=4, ensure_ascii=False)
    arquivo.close()

# Essa função é usada para mostrar um item individual da lista, 
def mostrar_item(item):
    print(f"id: {item["id"]} nome: {item["nome"]} preço: {item["preco"]} quantidade em estoque: {item["estoque"]}")

# Essa função é usada para requisitar a entrada de uma float
# caso a entrada seja qualquer coisa que não é uma float a função pede a entrada denovo até que a entrada seja uma float
def entrada_float(mensagem):
    while True:
        try:
            numero = input(mensagem)
            return float(numero)
        except ValueError:
            print("erro ao processar entrada, tente novamente")

# Faz a mesma coisa que entrada_float() mas pede por uma int
def entrada_int(mensagem):
    while True:
        try:
            numero = input(mensagem)
            return int(numero)
        except ValueError:
            print("erro ao processar entrada, tente novamente")

# mostra todos os produtos
def mostrar_produtos():
    produtos = carregar_produtos()
    for x in produtos:
        mostrar_item(x)
    print("")
    input("aperter ENTER par continuar")
    print("")


def procurar_produto():
    nome = input("Qual o nome do produto: ")
    produtos = carregar_produtos()
    for x in produtos:
        if nome.casefold() in x["nome"].casefold() :
            mostrar_item(x)
    print("")
    input("aperte ENTER para continuar")
    print("")

# usada por outras funções para procurar um produto usando o id
def procurar_id():
    produtos = carregar_produtos()
    while True:
        produto_id = entrada_int("digite o id do produto: ")
        id_valido = 0
        for x in produtos:
            if x["id"] == produto_id:
                produto = x
                id_valido = 1
                break
        if id_valido == 1:
            mostrar_item(produto)
            opt = input("esse é o produto correto [S/N]: ")

            if opt.lower() in ["sim", "s"]:
                return produto
                break
            elif opt.lower() in ["não", "n", "nao"]:
                print("tente novamente")
        else:
            print("id invalido tente novamente")

def registrar_entrada():
    produtos = carregar_produtos()
    produto = procurar_id()

    num = entrada_int("Quanto sera adiconado a o estoque: ")
    novo_valor = dict(produto)

    novo_valor["estoque"] = (produto["estoque"] + num)
    mostrar_item(novo_valor)

    while True:
        opt = input("Deseja comfirmar a operação [S/N]: ")
        if opt.lower() in ["sim", "s"]:
            index = produtos.index(produto)
            produtos[index] = novo_valor
            salvar_produtos(produtos)
            return 0
        
        elif opt.lower() in ["não", "nao", "n"]:
            print("operação cancelada")
            return 1
        
        else:
            print("erro ao processar entrada")

def registrar_saida():
    produtos = carregar_produtos()
    produto = procurar_id()

    num = entrada_int("Quanto sera deduzido a o estoque: ")
    novo_valor = dict(produto)

    novo_valor["estoque"] = (produto["estoque"] - num)
    mostrar_item(novo_valor)

    while True:
        opt = input("Deseja comfirmar a operação [S/N]: ")
        if opt.lower() in ["sim", "s"]:
            index = produtos.index(produto)
            produtos[index] = novo_valor
            salvar_produtos(produtos)
            return 0
        
        elif opt.lower() in ["não", "nao", "n"]:
            print("operação cancelada")
            return 1
        
        else:
            print("erro ao processar entrada")


while True:
    print("1 - mostrar todos os produtos")
    print("2 - procurar por produto")
    print("3 - registrar entrada")
    print("4 - registrar saida")
    print("5 - registrar produto")
    print("6 - alterar produto")
    print("7 - remover produto")
    print("0 - sair")
    print("")
    opt = input("selecione uma opção: ")

    if opt=="1":
        mostrar_produtos()
    elif opt=="2":
        procurar_produto()
    elif opt=="3":
        registrar_entrada()
    elif opt=="4":
        print(4)
    elif opt=="5":
        print(5)
    elif opt=="6":
        print(6)
    elif opt=="7":
        print(7)
    elif opt=="0":
        exit()
    else:
        print("opção invalida")