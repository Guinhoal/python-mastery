lista = []
print("Digite uma lista para receber um dicionário sem duplicadas:")
while True:
    print("Digite o elemento da lista (999 para parar):")
    elemento = int(input())
    if elemento == 999:
        break
    lista.append(elemento)

conjunto = set(lista)
print(conjunto)