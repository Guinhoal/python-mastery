# Descrição: Receber um número de linhas e colunas e preencher uma matriz com números digitados pelo usuário.

matriz = []
numero = 0.0
linhas = 0
colunas = 0

print("Digite as proporções da matriz, exemplo -> 3x4:")
print("Digite o número de linhas: ")
linhas = int(input())
print("Digite o número de colunas: ")
colunas = int(input())

print("Digite elementos numéricos para preencher a matriz. Caso queira sair, digite 999")

for p_linhas in range(linhas):
    linha = []
    for p_colunas in range(colunas):
        while True:
            print(f"Digite o número que estará na linha {p_linhas + 1} e na coluna {p_colunas + 1}:")
            numero = input()
            if numero == "999":
                print("Encerrando a entrada de dados.")
                break
            try:
                numero = float(numero)
                linha.append(numero)
                break
            except ValueError:
                print("Por favor, digite um número válido.")
    if numero == "999":
        break
    matriz.append(linha)

print("Matriz preenchida:")
for linha in matriz:
    print(linha)