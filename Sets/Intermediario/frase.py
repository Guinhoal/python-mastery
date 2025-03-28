# Descrição: Crie um programa que leia uma frase do usuário e retorne um conjunto 
# com todas as palavras únicas presentes na frase. O programa deve converter a frase 
# para minúsculas e dividir as palavras corretamente.

def palavras_unicas(frase):
    palavras = frase.lower().split() 
    unicas = set(palavras)  
    return unicas

frase = input("Digite uma frase: ")
print("Palavras únicas:", palavras_unicas(frase))
