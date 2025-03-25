#Descrição: Programe um algoritmo que comprima uma tupla registrando a contagem de elementos repetidos consecutivos. Por exemplo, (a,a,a,b,b,c) é comprimido para (3,a,2,b,1,c).
lista = []
tupla = ()
print("Digite uma tupla para ela ser comprimida")

def cria_tupla():
    while True:
        print("Digite o elemento da tupla (Para parar 999):")
        elemento = input()
        if elemento == "999":
            break
        lista.append(elemento)
    return tuple(lista)
    
tupla = cria_tupla()

def comprimi(tupla):
    if not tupla:
        return ()
        
    lista_final = []
    contador = 1
    elemento_atual = tupla[0]
    
    for i in range(1, len(tupla)):
        if tupla[i] == elemento_atual:
            contador += 1
        else:
            lista_final.append(contador)
            lista_final.append(elemento_atual)
            elemento_atual = tupla[i]
            contador = 1
    
    lista_final.append(contador)
    lista_final.append(elemento_atual)
    
    return tuple(lista_final)

final_tupla = comprimi(tupla)

print("Tupla comprimida")
print(final_tupla)
    


        