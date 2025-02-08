# Descrição: Programa que busca uma palavra em uma fraseT

print("Digite uma frase para buscar uma palavra:")
str_normal = str(input())
print("Digite a palvra que deseja buscar na frase:")
str_palavra = str(input())
indice = str_normal.find(str_palavra)
if indice == -1:
    print(f"A palavra: {str_palavra} não esta na frase: {str_normal}")
else:
    print(f"A palavra: {str_palavra} esta na frase: {str_normal} após {indice} caracteres")