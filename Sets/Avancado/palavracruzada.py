# Descrição: Crie um programa que leia duas listas de palavras e encontre as 
# palavras que aparecem em ambas as listas. O programa deve converter as listas 
# para conjuntos e usar a função intersection() para encontrar as palavras 
# idênticas. A leitura deve parar quando o usuário digitar '999'.

print("Digite duas listas de palavras para encontrar idênticos")

def cria_lista(num):
    lista = []
    print(f"Digite a lista {num}")
    while True:
        print("Digite a palavra da lista (999 para parar)")
        elemento = input()
        if elemento == '999':
            break
        lista.append(elemento)
    conjunto = set(lista)
    return conjunto

conjunto1 = cria_lista(1)
conjunto2 = cria_lista(2)


palavras_repetidas = conjunto1.intersection(conjunto2)

print(palavras_repetidas)