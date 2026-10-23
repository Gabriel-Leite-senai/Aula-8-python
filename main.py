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

def confirmar_operacao(produtos):
    while True:
        opt = input("Deseja comfirmar a operção[S/N]? ")
        if opt.lower() in ["sim", "s"]:
            salvar_produtos(produtos)
            return 0
        elif opt.lower() in ["não", "n", "nao"]:
            print("operação cancelada")
            return 1
        else:
            print("opção invalida")

# Essa função é usada para mostrar um item individual da lista, 
def mostrar_item(item):
    print(f"id: {item["id"]} nome: {item["nome"]} categoria: {item["categoria"]} preço: {item["preco"]} quantidade em estoque: {item["estoque"]}")

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

# procura item por nome
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
    index = produtos.index(produto)
    produtos[index] = novo_valor

    confirmar_operacao(produtos)
    
def registrar_saida():
    produtos = carregar_produtos()
    produto = procurar_id()
    while True:
        num = entrada_int("Quanto sera deduzido a o estoque: ")
        if num <= produto["estoque"]:
            break
        else:
            print("o numero a ser deduzido do estoque não pode ser maior que o numero em estoque")
            
    novo_valor = dict(produto)

    novo_valor["estoque"] = (produto["estoque"] - num)
    mostrar_item(novo_valor)
    index = produtos.index(produto)
    produtos[index] = novo_valor

    confirmar_operacao(produtos)

def selecionar_categoria(mensagen):
    while True:
        print("1 - Armazenamento")
        print("2 - Periféricos")
        print("3 - Informatica")
        print("4 - Redes")
        print("5 - Outros")

        opt = input(mensagen)
        if opt == "1":
            return "Armazenamento"
        elif opt == "2":
            return "Periféricos"
        elif opt == "3":
            return "Informatica"
        elif opt == "4":
            return "Redes"
        elif opt == "5":
            return "Outros"
        else: 
            print("opção invalida tente novamente")

def registrar_novo_produto():
    produtos = carregar_produtos()
    nome = input("Digite o nome do produto a ser registrado: ")
    preco = entrada_float("Digite o preço do produto: ")
    estoque = entrada_int("Digite a quantidade em estoque: ")

    categoria = selecionar_categoria("selecione a categoria do produto: ")
    
    novo_id = 1
    for x in produtos:
        if x["id"] == novo_id:
            novo_id +=1
        else:
            break

    novo_item = {"id": novo_id, "nome": nome, "categoria": categoria, "preco": preco, "estoque":estoque}
    produtos.append(novo_item)
    mostrar_item(novo_item)
    
    confirmar_operacao(produtos)

def alterar_produto():
    produto = procurar_id()

    while True:
        print("1 - nome")
        print("2 - categoria")
        print("3 - preço")

        opt = input("qual a caracteristica que deve ser alterada: ")
        if opt == "1":
            novo_valor = input("qual o sera o novo nome do produto: ")
            c = "nome"
            break
        elif opt == "2":
            novo_valor = selecionar_categoria("Qual o nova categoria do produto: ")
            c = "categoria"
            break
        elif opt == "3":
            novo_valor = entrada_float("qual sera o novo preço do produto: ")
            c = "preco"
            break
        else:
            print("opção invalida, tente novamente")
    produto_alterado = dict(produto)
    produto_alterado[c] = novo_valor
    mostrar_item(produto_alterado)

    produtos = carregar_produtos()
    index = produtos.index(produto)
    produtos[index] = dict(produto_alterado)

    confirmar_operacao(produtos)

def remover_produto():
    produto = procurar_id()
    produtos = carregar_produtos()

    produtos.remove(produto)
    confirmar_operacao(produtos)


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
        registrar_saida()
    elif opt=="5":
        registrar_novo_produto()
    elif opt=="6":
        alterar_produto()
    elif opt=="7":
        remover_produto()
    elif opt=="0":
        exit()
    else:
        print("opção invalida")