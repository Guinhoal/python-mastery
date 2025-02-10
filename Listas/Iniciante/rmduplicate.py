#Descrição: Escreva um programa que leia uma lista de números e mostre os números sem duplicatas.
lista = []
print("Digite elementos para retirar os duplicados, quando acabar digite 'sair'")
while True:
    print("Digite um elemento:")
    elemento = input()
    if elemento == 'sair' or elemento == 'Sair' or elemento == "SAIR":
        break
    else:
        lista.append(elemento)

sem_duplicadas = list(set(lista))
sem_duplicadas.sort()
print("Itens sem duplicadas: ")
for _ in sem_duplicadas:
    print(_)
