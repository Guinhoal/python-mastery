#Descrição: Programe um algoritmo que desempacota uma tupla. Se a tupla tiver 3 elementos ou menos, imprime cada elemento individualmente. Se tiver mais, imprime os 3 primeiros como uma tupla e o restante individualmente.
lista = []
tupla = ()

print("Digite uma tupla para ela ser desempacotada:")
while True:
    print("Digite o elemento (para parar 999):")
    elemento = int(input())
    if elemento == 999:
        break
    lista.append(elemento)

tupla = tuple(lista)

def desempacota(tupla):
    tamanho = len(tupla)
    lista2 = []
    tupla2 = ()
    if tamanho <= 3:
        for elemento in tupla:
            print(elemento)
    else:
        for i in range(3):
            lista2.append(tupla[i])
        tupla2 = tuple(lista2)
        print(tupla2)
        for i in range(3, tamanho):
            print(tupla[i])

desempacota(tupla)            
        
