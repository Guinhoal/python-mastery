#Descrição: Faça um programa realiza a contagem de quantas vezes cada caractere aparece em uma string

print("Digite uma string para realizar uma contagem de quantas vezes cada caractere aparece:")
string_usada = str(input())
string_usada = string_usada.lower()

def adiciona_espaco_virgula(letra, dicionario):
    if letra == " ":
        if "espaco" in dicionario:
            dicionario["espaco"] += 1
        else:
            dicionario["espaco"] = 1
    elif letra == ",":
        if "virgula" in dicionario:
            dicionario["virgula"] += 1
        else:
            dicionario["virgula"] = 1
    else:
        return


dicionario = {}

for letra in string_usada:
    if letra in dicionario and letra != " " and letra != ",":
        dicionario[letra] += 1
    else:
        if letra != " " and letra != ",":
            dicionario[letra] = 1
        else:
            adiciona_espaco_virgula(letra, dicionario)


print("Contagem dos caracteres:")
for _ in dicionario.keys():
    print(f"{_}: {dicionario[_]}")
