def palavras_unicas(frase):
    palavras = frase.lower().split() 
    unicas = set(palavras)  
    return unicas

frase = input("Digite uma frase: ")
print("Palavras únicas:", palavras_unicas(frase))
