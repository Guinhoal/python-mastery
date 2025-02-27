import random

print("Iremos jogar o jogo da vida ou Conways Life")
print("Caso queria saber mais sobre deve ver o comentário ou pesquisar")
print("Inicialmente digite a ordem da matriz (mínimo 3, máximo 8)")

ordem_matriz = int(input())

if ordem_matriz < 3:
    ordem_matriz = 3
elif ordem_matriz > 8:
    ordem_matriz = 8

matriz = []

for linhasn in range(ordem_matriz):
    linhas = []
    for colunas in range(ordem_matriz):
        linhas.append(random.randint(0, 1))
    matriz.append(linhas)

print(matriz)