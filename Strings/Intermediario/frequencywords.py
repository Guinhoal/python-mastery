# Descrição: Faça um programa que leia uma frase e exiba a frequência de cada palavra na frase.
# Exemplo: "eu gosto de estudar e eu gosto de jogar" -> eu: 2, gosto: 2, de: 2, estudar: 1, e: 1, jogar: 1

print("Digite uma frase e veja a frequência de cada palavra: ")
normal_str = str(input())
lista_str = normal_str.split(" ")
dicionario = {}
for palavra in lista_str:
    if palavra in dicionario:
        dicionario[palavra] += 1
    else:
        dicionario[palavra] = 1

print("Frequência das palavras:")
for _ in dicionario.keys():
    print(f"{_}: {dicionario[_]}")