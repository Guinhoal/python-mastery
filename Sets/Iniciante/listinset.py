# Descrição: Crie um programa que leia uma sequência de números inteiros para uma 
# lista e depois converta essa lista em um conjunto (set) para eliminar duplicatas.
# O programa deve parar de ler números quando o usuário digitar 999.

lista = []
print("Digite uma lista para receber um dicionário sem duplicadas:")
while True:
    print("Digite o elemento da lista (999 para parar):")
    elemento = int(input())
    if elemento == 999:
        break
    lista.append(elemento)

conjunto = set(lista)
print(conjunto)