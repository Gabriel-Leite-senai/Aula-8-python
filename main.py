import json

def carregar_produtos():
    arquivo = open("produtos.json", "r", encoding="utf-8")
    produtos = json.load(arquivo)
    arquivo.close()
    return produtos

def salvar_produtos(produtos):
    arquivo open("produtos.json", "w", encoding="utf-8")
    json.dump(produtos, arquivo, indent=4, ebsure_ascii=False)
    arquivo.close()

while True:
    print("1 - mostrar produtos")
    print("2 - registrar entrada")
    print("3 - registrar saida")
    print("4 - registrar produto")
    print("5 - alterar produto")
    print("6 - remover produto")
    print("0 - sair")

    opt = input("selecione uma opção: ")

    if opt="1":
        print(1)
    elif opt="2":
        print(2)
    elif opt="3":
        print(3)
    elif opt="4":
        print(4)
    elif opt="5":
        print(5)
    elif opt="6"
        print(6)
    elif opt="0":
        exit()
    else:
        print("opção invalida")