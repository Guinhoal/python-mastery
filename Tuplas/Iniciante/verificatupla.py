#Descrição: Programe um algoritmo que verifica se um elemento específico existe em uma tupla e conta quantas vezes ele aparece.
lista = []
tupla = ()

print("Digite os elementos da tupla para parar (999)")
while True:
    print("Digite o elemento: ")
    elemento = int(input())
    if elemento == 999:
        break
    lista.append(elemento)

tupla = tuple(lista)

print("Digite o elemento que deseja buscar na tupla:")
elemento_2 = int(input())
verificar = tupla.count(elemento_2)

if verificar == 0:
    print("Não possui este elemento na tupla")
else:
    print(f"Este elemento aparece {verificar} vezes na lista")