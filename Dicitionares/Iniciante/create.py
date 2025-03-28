def cria_dic():
    dicionario = {}
    print("Cire um dicionário para depois exibi-lo")
    while True:
        print("Digite a chave (999 para parar)")
        elemento = input()
        if elemento == '999':
            break
        print("Digite o valor (999 para parar)")
        elemento2 = input()
        if elemento2 == '999':
            break
        dicionario[elemento] = elemento2
    return dicionario

dicionario = cria_dic()

print(dicionario)