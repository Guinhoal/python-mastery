lista = []
tupla = ()

print("Digite uma tupla e receba ela ordenada")
while True:
    print("Digite o elemento (para parar 999):")
    elemento = int(input())
    if elemento == 999:
        break
    lista.append(elemento)

print("Primeira forma:")
lista.sort()
tupla2 = tuple(lista)
print(tupla2)

print("Segunda forma:")
lista_copia = lista.copy()
n = len(lista_copia)
for i in range(n):
    for j in range(0, n-i-1):
        if lista_copia[j] > lista_copia[j+1]:
            lista_copia[j], lista_copia[j+1] = lista_copia[j+1], lista_copia[j]

tupla_ordenada = tuple(lista_copia)
print(tupla_ordenada)