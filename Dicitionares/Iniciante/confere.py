
print("Insira um dicionário e depois verifique se uma chave existe:")

def cria_dicionario():
    print("Insira o dicionario")
    contador = 1
    dicionario = dict()
    while True:
        print(f"Digite a chave {contador} (999 para parar)")
        chave = input()
        if chave == "999":
            break
        print(f'Digite o valor de "{chave}"')
        valor = input()
        dicionario[chave] = valor
        contador += 1
    return dicionario

dicionario = cria_dicionario()

print("Digite a chave que deseja buscar:")

busca = input()

if busca in dicionario.keys():
    print("A chave esta no dicionario")
else:
    print("A chave não esta no dicionario")
