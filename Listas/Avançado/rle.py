# Descrição: Faça um programa que leia uma lista de números e retorne uma lista com as sequências de números repetidos.
# Exemplo: entrada = [1, 1, 1, 2, 2, 3, 3, 3, 3] saida   = [(1, 3), (2, 2), (3, 4)]

lista = []
new_lista = []
print("Preencha a lista com sequências de carecteres que viraram pares")
print("Exemplo: entrada = [A, A, A, B, B, C, C, C, C] saida   = [(A, 3), (B, 2), (C, 4)]")

while True:
    print("Digite o elemento (para parar digite SAIR): ")
    velement = str(input())
    if velement.upper() == "SAIR":
        break
    lista.append(velement)

i = 0
while i < len(lista):
    count = 1
    while (i + count) < len(lista) and lista[i] == lista[i + count]:
        count += 1
    new_lista.append((lista[i], count))
    i += count

print(new_lista)
