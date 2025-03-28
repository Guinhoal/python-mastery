print("Insira um dicionário e depois remova uma chave:")

def cria_dicionario():
    print("Crie seu dicinário")
    contador = 1
    dicionario = dict()
    while True:
        print(f"Digite a chave {contador} (999 para parar)")
        chave = input()
        if chave == '999':
            break
        print(f'Digite o valor de "{chave}"')
        valor = input()
        dicionario[chave] = valor
        contador += 1
    return dicionario

dicionario = cria_dicionario()
copia = dicionario

print("Digite a chave que deseja excluir:")
excluir = input()

print("Forma 1:")

for chaves in dicionario.keys():
    if excluir.lower() == chaves.lower():
        del dicionario[chaves]
        break

print(dicionario)

print("Forma 2:")

copia.pop(excluir, "Não encontrado")

print(dicionario)





