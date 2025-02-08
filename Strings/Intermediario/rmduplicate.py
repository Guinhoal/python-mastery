print("Digite a String que deseja remover aracteres duplicados:")
str_normal = str(input())
str_normal = str_normal.lower()
lista_duplicate = []
str_mostrar = ""

def reconhece_duplicada(str_normal):
    str_nova = ""
    for letra in str_normal:
        if letra in lista_duplicate:
            continue
        else: 
            lista_duplicate.append(letra)
            str_nova += letra
    return str_nova

str_mostrar = reconhece_duplicada(str_normal)
print(f"String sem caracteres duplicados; {str_mostrar}")

        