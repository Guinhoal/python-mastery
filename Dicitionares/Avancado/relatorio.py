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
        print(f"Digite o preço do {produto}:")
        preco = float(input())
        print(f"Digite a quantidade de {produto} vendidos")
        quantidade = int(input())
        dicionario[produto] = (preco, quantidade)
        contador += 1
    return dicionario

dicionario = cria_dicionario()

def faz_relatorio(dicionario):
    valores = []
    for chave in dicionario.keys():
        valores.append(dicionario[chave][0] * dicionario[chave][1] )
    valor_total = sum(valores)
    media = valor_total/len(valores)
    quantidade_vendas = 0
    for chave in dicionario.keys():
        quantidade_vendas += dicionario[chave][1]
    return print(f"---------------------------------------------------------------\n Valor Total: {valor_total} \n Valor Médio: {media} \n Quantidade de vendas: {quantidade_vendas} \n ------------------------------------------------------------------")

faz_relatorio(dicionario)
