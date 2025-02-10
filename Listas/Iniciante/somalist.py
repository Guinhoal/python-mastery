#Descrição: Faça um programa que leia uma lista de números e some todos os elementos da lista. O programa deve encerrar quando o usuário digitar 999.
lista = []
soma = 0
numero = 0.0
print("Digite elementos númericos e depois veja a soma de todos caso queira encerrar digite 999")
while True:
    print("Digite o número:")
    numero = float(input())
    if int(numero) == 999:
        break
    else: 
        lista.append(numero)

soma = sum(lista)
print(f"A soma dos valores é igual a {soma}")
    
    





