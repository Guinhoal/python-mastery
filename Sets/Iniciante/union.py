print("Insira dois conjuntos e veja a união dos dois:")

def cria_conjunto(num):
    conjunto = set()
    print(f"Digite o conjunto {num}")
    while True:
        print("Digite o elemento (999 para parar):")
        elemento = int(input())
        if elemento == 999:
            break
        conjunto.add(elemento)
    return conjunto
    
conjunto1 = cria_conjunto(1)
conjunto2 = cria_conjunto(2)

conjunto3 = conjunto1.union(conjunto2)

print(conjunto3)