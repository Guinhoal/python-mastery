#Descrição: Faça um programa que leia um número inteiro e gere uma matriz identidade de ordem n.
# Uma matriz identidade é uma matriz quadrada em que todos os elementos da diagonal principal são iguais a 1 e todos os outros elementos são iguais a 0.

ordem_matriz = 0
print("Digite a ordem da matriz a ser feitra a identidade.")
print("Ex: ordem 3 = 3x3 -- Digite a ordem:")
ordem_matriz = int(input())

matriz = []
cont_ex = 1
cont = 1

for linhasn in range(ordem_matriz):
    linhas = []
    for colunas in range(ordem_matriz):
        if cont == cont_ex:
            linhas.append(1)
            cont += 1
        else:
            linhas.append(0)
            cont += 1
    
    cont = 1
    matriz.append(linhas)
    cont_ex += 1

for linhas in matriz:
    print(linhas)

