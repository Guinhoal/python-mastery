#Descrição: Programe um algoritmo que cria uma tupla contendo apenas o primeiro e o último elemento de uma lista fornecida pelo usuário.

print("Digite uma lista de elementos para colocar o primeiro e ultimo em uma tupla:")
lista = []
while True:
    print("Digite um elemento (999 para sair)")
    elemento = int(input())
    if elemento == 999:
        break
    lista.append(elemento)

tupla = (lista[0], lista[len(lista) - 1 ])
print("Tupla com o primeiro e último elemento:")
print(tupla)
