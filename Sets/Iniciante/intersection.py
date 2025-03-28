# Descrição: Crie um programa que leia dois conjuntos de números inteiros e 
# retorne a interseção entre eles. O programa deve usar a função intersection() 
# dos sets e parar de ler números para cada conjunto quando o usuário digitar 999.

print("Digite dois conjuntos para ver a interseção entre eles")

def cria_conjunto(num):
    print(f"Digite o conjunto {num}")
    conjunto = set()
    while True:
        print("Digite o elemento (999 para parar)")
        elemento = int(input())
        if elemento == 999:
            break
        conjunto.add(elemento)
    return conjunto

conjunto1 = cria_conjunto(1)
conjunto2 = cria_conjunto(2)

conjunto3 = conjunto1.intersection(conjunto2)

print("Interseção")
print(conjunto3)