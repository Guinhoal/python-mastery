def cria_tupla(num_tupla):
    tupla = ()
    lista = []
    print(f"Crie sua tupla {num_tupla} digitando os elementos para parar digite (999)")
    while True:
        print("Digite o elemento: ")
        elemento = int(input())
        if elemento == 999:
            break
        lista.append(elemento)
    tupla = tuple(lista)
    return tupla

tupla1 = cria_tupla(1)
tupla2 = cria_tupla(2)

soma = tupla1 + tupla2

print("A concatenação das tuplas tem como resposta:")
print(soma)
