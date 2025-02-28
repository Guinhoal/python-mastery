import random
import time

def criar_matriz(ordem):
    return [[random.randint(0, 1) for _ in range(ordem)] for _ in range(ordem)]

def imprime_tabuleiro(matriz):
    for linha in matriz:
        print(" ".join(str(celula) for celula in linha))
    print()

def contar_vizinhos(matriz, x, y):
    ordem = len(matriz)
    vizinhos = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),         (0, 1),
        (1, -1), (1, 0), (1, 1)
    ]
    soma = 0
    for dx, dy in vizinhos:
        nx = (x + dx) % ordem
        ny = (y + dy) % ordem  
        soma += matriz[nx][ny]
    return soma

def proxima_geracao(matriz):
    ordem = len(matriz)
    nova_matriz = [[0] * ordem for _ in range(ordem)]
    
    for i in range(ordem):
        for j in range(ordem):
            vivos = contar_vizinhos(matriz, i, j)
            if matriz[i][j] == 1:
                nova_matriz[i][j] = 1 if vivos in (2, 3) else 0
            else:
                nova_matriz[i][j] = 1 if vivos == 3 else 0
                
    return nova_matriz

def jogo_da_vida():
    print("Iremos jogar o Jogo da Vida de Conway!")
    ordem = int(input("Digite a ordem da matriz (mínimo 3, máximo 8): "))
    ordem = max(3, min(8, ordem))

    matriz = criar_matriz(ordem)
    print("Tabuleiro Inicial:")
    imprime_tabuleiro(matriz)

    while True:
        time.sleep(1)
        matriz = proxima_geracao(matriz)
        imprime_tabuleiro(matriz)
        if sum(sum(linha) for linha in matriz) == 0:
            print("Todas as células morreram. O jogo acabou.")
            break

jogo_da_vida()
