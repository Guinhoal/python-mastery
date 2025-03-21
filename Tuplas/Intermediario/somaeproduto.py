print("Digite uma tupla para ver a soma do seus elementos e o produto:")
lista = []
tupla = ()
while True:
    print("Digite o elemento (Para parar 999):")
    elemento = int(input())
    if elemento == 999:
        break
    lista.append(elemento)

tupla = tuple(lista)

soma = sum(tupla)
produto = 1.0

for elementos in tupla:
    produto *= elementos

print(f"Soma = {soma}")
print(f"Produto = {produto}")

