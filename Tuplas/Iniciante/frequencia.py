tupla = ()
lista = []

print("Digite a tupla que deseja ver a frequência para parar (999)")
while True:
    print("Digite o elemento:")
    elemento = int(input())
    if elemento == 999:
        break
    lista.append(elemento)

tupla = tuple(lista)

dicionario = {}

for elemento in tupla:
    if elemento in dicionario:
        dicionario[elemento] += 1
    else:
        dicionario[elemento] = 1

print(dicionario)