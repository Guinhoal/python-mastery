print("Digite elementos para sua tupla. (Caso deseje parar digite 999)")
tupla = ()
lista = []

while True:
    print("Digite o elemento: ")
    elemento = int(input())
    if elemento == 999:
        break
    lista.append(elemento)

tupla = tuple(lista)

print(tupla)