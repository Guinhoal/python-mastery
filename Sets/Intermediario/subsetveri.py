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

if conjunto1.issubset(conjunto2):
    print("O conjunto 1 é subconjunto do conjunto 2")
elif conjunto2.issubset(conjunto1):
    print("O conjunto 2 é subconjunto do conjunto 1")
else:
    print("Nenhum conjunto é subconjunto do outro")


