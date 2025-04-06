print("Digite dois dicionários e depois veja eles juntos em um só")

def cria_dicionario(num):
    print(f"Digite o dicionario {num}")
    dicionario = dict()
    contador = 1
    while True:
        print(f"Digite a chave {contador} (999 para parar):")
        chave = input()
        if chave == "999":
            break
        print(f"Digite o valor da chave {chave}:")
        valor = input()
        dicionario[chave] = valor
        contador += 1
    return dicionario

dicionario1 = cria_dicionario(1)
dicionario2 = cria_dicionario(2)

chaves_para_remover = [chave for chave in dicionario2.keys() if chave in dicionario1.keys()]

for chave in chaves_para_remover:
    del dicionario2[chave]

for chave in dicionario2.keys():
    dicionario1[chave] = dicionario2[chave]

print("Dicionário Unico:")

print(dicionario1)


