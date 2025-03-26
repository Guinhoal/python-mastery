print("Digite 2 conjuntos e veja se um conjunto é subcojunto do outro:")

def cria_conjunto(num):
    conjunto = set()
    print(f"Digite os elementos do conjunto {num}")
    while True:
        print("Digite o elemento (999 para parar)")
        elemento = int(input())
        if elemento == 999:
            break
        conjunto.add(elemento)
    return conjunto

conjunto1 = cria_conjunto(1)
conjunto2 = cria_conjunto(2)

conjunto3 = conjunto1 - conjunto2
conjunto4 = conjunto2 - conjunto1

print("Conjunto 1 menos conjunto 2:")
print(conjunto3)

print("Conjunto 2 menos conjunto 1:")
print(conjunto4)