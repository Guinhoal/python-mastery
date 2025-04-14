print("Digite um dicionário dentro de um dicionário e depois busque informações")

def cria_dicionario(contexto=None):
    dicionario = {}
    if contexto == None:
        print("Insira seu primeiro Dicionário:")
    else:
        print(f"Insira o dicionário dentro de {contexto}")
    
    contador = 1
    while True:
        print(f"Insira a chave {contador} - (999 para parar)")
        chave = input()
        if chave == '999':
            break
        
        print(f"Insira o valor para a chave '{chave}':")
        print("1 - Valor simples")
        print("2 - Novo dicionário")
        escolha = input("Escolha uma opção: ")
        
        if escolha == '1':
            valor = input("Digite o valor: ")
            dicionario[chave] = valor
        elif escolha == '2':
            dicionario[chave] = cria_dicionario(chave)
        else:
            print("Opção inválida, tente novamente.")
            continue
        
        contador += 1
    
    return dicionario

def busca_informacao(dicionario):
    print("\nAgora vamos buscar informações no dicionário:")
    print(f"Seu dicionário: {dicionario}")
    
    while True:
        chave = input("\nDigite a chave que deseja buscar (999 para sair): ")
        if chave == '999':
            break
        
        if chave in dicionario:
            valor = dicionario[chave]
            print(f"Valor encontrado: {valor}")
            
            if isinstance(valor, dict) and valor:
                continuar = input("Este valor é um dicionário. Deseja explorar? (s/n): ")
                if continuar.lower() == 's':
                    busca_informacao(valor)
        else:
            print("Chave não encontrada!")

dicionario_principal = cria_dicionario()
busca_informacao(dicionario_principal)