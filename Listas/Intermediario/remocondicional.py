#Descrição: Faça um programa que leie uma lista de números e retorne uma lista com os números pares inclusos na lista.

lista = []
new_lista = []
numero = 0
print("Digite numeros para retirarmos os ímpares caso queira parar digite 999")
while True:
    print("Digite o número: ")
    numero = int(input())
    if numero == 999:
        break
    else:
        lista.append(numero)

for it in lista:
    if (it % 2 == 0) or it == 0:
        new_lista.append(it)
    else:
        continue

print (new_lista)

print("Segunda forma")

for ind in range(len(lista) -1, -1, -1):
    if (lista[ind] % 2 == 0) or lista[ind] == 0:
        continue
    else:
        lista.pop(ind)

print(lista)
