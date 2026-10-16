import json

def carregar_produtos():
    arquivo = open("produtos.json", "r", encoding="utf-8")
    produtos = json.load(arquivo)
    arquivo.close()
    return produtos

def salvar_produtos(produtos):
    arquivo = open("produtos.json", "w", encoding="utf-8")
    json.dump(produtos, arquivo, indent=4, ebsure_ascii=False)
    arquivo.close()

# Essa função é usada para mostrar um item individual da lista, 
def mostrar_item(item):
    print(f"id: {item["id"]} nome: {item["nome"]} preço: {item["preco"]} quantidade em estoque: {item["estoque"]}")

def entrada_num(mensagem):
    while True:
        try:
            numero = input(mensagem)
            return float(numero)
        except ValueError:
            print("erro ao processar entrada, tente novamente")

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

def registrar_entrada():
    produtos = carregar_produtos()
    while True:
        produto_id = entrada_num("digite o id do produto: ")
        id_valido = 0
        for x in produtos:
            if x["id"] == produto_id:
                produto = x
                id_valido = 1
                break
        if id_valido = 1:
            mostrar_item(produto)
            opt = input("esse é o produto correto [S/N]: ")

            if opt.lower() in ["sim", "s"]:
                print("AAAA")
                break
            elif opt.lower() in ["não", "n", "nao"]:
                print("tente novamente")
        else:
            print("id invalido tente novamente")

    num = entrada_num("Quanto sera adiconado a o estoque: ")
    novo_valor = produto

    novo_valor["estoque"] = produto["estoque"] + num

    mostrar_item(novo_valor)
    opt = input("Deseja comfirmar a operação")
    if opt.lower() = ["sim", "s"]



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