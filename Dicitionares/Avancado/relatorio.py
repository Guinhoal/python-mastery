print("Digite um dicionário com produtos seguidos de preços e unidades vendidas:")

def cria_dicionario():
    print("Digite o Dicionário com as informações:")
    dicionario = dict()
    contador = 1
    while True:
        print(f"Digite o nome do produto {contador}, (999 - para parar):")
        produto = input()
        if produto == "999":
            break