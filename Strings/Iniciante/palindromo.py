# Descrição: Verifica se a palavra digitada é um palíndromo

print("Digite a palavra que deseja verificar se é um palíndromo: ")
str_usada = str(input())
if str_usada == str_usada[::-1]:
    print("A palavra digitade é um palíndromo")
else: 
    print("A palavra digitada não é um palíndromo")