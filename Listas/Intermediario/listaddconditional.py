# Descrição: Crie um programa que leia uma sequência de números e retorne uma 
# lista com os quadrados dos números pares e outra lista com todos os quadrados. 
# O programa deve parar de ler números quando o usuário digitar 999.   

lista1 = []
lista2 = []
lista3 =[]
numero = 0
print("Digite uma sequência de número e será retornado uma sequência com os quadrados dos pares, caso deseje para insira 999")
while True:
    print("Digite um número")
    numero = int(input())
    if numero == 999:
        break
    else:
        lista1.append(numero)

lista2 = [num**2 for num in lista1 ]

print("Lista com todos números ao quadrado:")
print(lista2)

for num in lista1:
    if num % 2 == 0 or num == 0:
        lista3.append(num**2)
print("Somente com os números pares:")
print(lista3)
