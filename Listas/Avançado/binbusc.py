# Descrição: Faça um programa que leia uma lista de números e um valor para ser buscado na lista.
# Utilize o algoritmo de busca binária para encontrar o valor na lista.

lista = []
busca = 0.0

print("Digite uma lista para encontrarmos um valor através de busca binária ")

while True:
    print("Digite o elemento, caso queria sair digite 999")
    elemento = float(input())
    if elemento == 999:
        break
    else:
        lista.append(elemento)


def binary_busca(lista, alvo):
    inicio = 0
    fim = len(lista) - 1

    while inicio <= fim:
        meio = (fim + inicio) // 2
        if lista[meio] == alvo:
            return meio
        elif lista[meio] < alvo:
            inicio = meio + 1
        elif lista[meio] > alvo:
            fim = meio - 1
    
    return -1


lista.sort()
print("Digite o elemento a ser buscado binariamente: ")
busca = float(input())
resultado = binary_busca(lista, busca)
if resultado == -1:
    print("O elemento buscado não esta na lista")
else: 
    print(f"O elemento bsucado esta na lista na posição {resultado + 1}")



