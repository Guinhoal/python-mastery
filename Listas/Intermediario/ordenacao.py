# Descrição: Organizar uma lista de números em ordem crescente sem usar o método sort.
lista = []
lista_ordenada = []
numero = 0.0
print("Digite numeros para poder serem organizados em ordem sem usar sort, caso queria parar digite 'sair'")
while True:
    print("Digite o número: ")
    numero = input()
    if numero == "sair" or numero == "SAIR" or numero == "Sair":
        break
    else:
        numero = float(numero)
        lista.append(numero)


n = len(lista)
for i in range(n):
    for j in range(0, n-i-1):
        if lista[j] > lista[j+1]:
            lista[j], lista[j+1] = lista[j+1], lista[j]

print("Lista ordenada:", lista)

    
