#Descrição: Programe um algoritmo que cria uma tupla de tuplas, onde cada tupla interna representa um par de chave-valor inserido pelo usuário.

pares = []
tupla_final = ()

print("Digite pares de chave-valor para criar uma tupla de tuplas")
print("Para cada par, você informará uma chave e um valor")

while True:
    print("\nDigite a chave (ou 'sair' para finalizar):")
    chave = input()
    
    if chave.lower() == 'sair':
        break
    
    print(f"Digite o valor para '{chave}':")
    valor = input()
    
    par = (chave, valor)
    pares.append(par)

tupla_de_pares = tuple(pares)

print("\nTupla de Tuplas criada:")
print(tupla_de_pares)

print("\nMostrando cada par:")
for par in tupla_de_pares:
    chave, valor = par
    print(f"Chave: '{chave}' --> Valor: '{valor}'")
