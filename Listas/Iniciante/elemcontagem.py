#Descrição : Programa que conta quantas vezes um elemento aparece em uma lista
lista = []
elemento = None
print("Digite elementos para fazer a contagem de quantos vezes cada elemento aparece caso queira para digite 'sair'")
while True:
    print("Digite o elemento:")
    elemento = input()
    if elemento == "sair" or elemento == "SAIR" or elemento == "Sair":
        break
    else:
        lista.append(elemento)

dicionario = {}

for elementou in lista:
    if elementou in dicionario:
        dicionario[elementou] += 1
    else:
        dicionario[elementou] = 1

for chaves in dicionario.keys():
    print(f"{chaves} aparece na lista {dicionario[chaves]} vezes")