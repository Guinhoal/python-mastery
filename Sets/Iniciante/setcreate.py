print("Digite elementos e depois veja o conjunto")
print("Lembre-se que sets não possuem duplicatas")

set1 = set()

while True:
    print("Digite o elemento do conjunto (999 para parar):")
    elemento = int(input())
    if elemento == 999:
        break
    set1.add(elemento)

print(set1)