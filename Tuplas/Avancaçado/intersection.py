print("Digite duas tuplas para poder juntar elas:")

def cria_tupla(num):
    lista = []
    print(f"Digite os elementos da tupla {num}")
    while True:
        print("Digite o elemento (999 para parar):")
        elemento = int(input())
        if elemento == 999:
            break
        lista.append(elemento)
    tupla = tuple(lista)
    return tupla

tupla1 = cria_tupla(1)
tupla2 = cria_tupla(2)

def junta_tupla(tupla1, tupla2):
    conjunto1 = set(tupla1)
    conjunto2 = set(tupla2)
    conjunto3 = conjunto1.intersection(conjunto2)
    tupla_correta = tuple(conjunto3)
    return tupla_correta

tupla_mostrar = junta_tupla(tupla1, tupla2)

print("Tupla com somente elementos presentas nas duas")
print(tupla_mostrar)