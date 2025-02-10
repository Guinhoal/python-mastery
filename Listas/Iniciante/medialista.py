#Descrição: Faça um programa que leia uma lista e diga a média dos elementos da lista.
lista = []
media = 0.0
numero = 0.0

print("Digite números para saber sua média para encerrar digite 999")
while True:
    print("Digite o elemento: ")
    numero = float(input())
    if int(numero) == 999:
        break
    else:
        lista.append(numero)

media = sum(lista) / len(lista)
print(f"A média dos elementos é {media}")
