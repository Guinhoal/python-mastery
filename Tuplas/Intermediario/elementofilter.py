#Descrição: Programe um algoritmo que cria uma tupla com diversos elementos e filtra apenas os valores numéricos, criando uma nova tupla apenas com esses valores.
lista = []
tupla = ()
lista_numericos = []

print("Digite uma tupla para ter retornado uma com somente os valores númericos")
while True: 
    entrada = input("Digite o elemento a ser adicionado (999 para parar): ")
    
    if entrada == "999":
        break
    try:
        if '.' in entrada:
            valor = float(entrada)
        else:
            valor = int(entrada)
        lista.append(valor)
    except ValueError:
        lista.append(entrada)

print("Tupla com todos seus elementos:")
tupla = tuple(lista)
print(tupla)

for elemento in lista:
    if isinstance(elemento, (int, float)):
        lista_numericos.append(elemento)
    
tupla_numericos = tuple(lista_numericos)

print("Tupla com apenas elementos númericos:")
print(tupla_numericos)