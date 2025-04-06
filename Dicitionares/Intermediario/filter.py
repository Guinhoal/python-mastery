print("Digite um dicionário para ser filtrado")

def cria_dicionario():
    print("Digite o dicionário:")
    dicionario = dict()
    contador = 1
    while True:
        print(f"Digite a chave {contador}, (999 para parar)")
        chave = input()
        if chave == "999":
            break
        print(f"Digite o valor da chave {chave}:")
        valor = input()
        contador += 1
        dicionario[chave] = valor
    return dicionario

dicionario = cria_dicionario()

print("Deseja filtrar seu dicionário pela chave ou valor ?")
opcao = input("Digite 'chave' ou 'valor': ").lower()

if opcao == "chave":
    filtro = input("Digite o texto para filtrar as chaves: ")
    resultado = {k: v for k, v in dicionario.items() if filtro in k}
    print("\nDicionário filtrado por chave:")
elif opcao == "valor":
    filtro = input("Digite o texto para filtrar os valores: ")
    resultado = {k: v for k, v in dicionario.items() if filtro in v}
    print("\nDicionário filtrado por valor:")
else:
    print("Opção inválida. Mostrando dicionário original.")
    resultado = dicionario

if resultado:
    print("\nResultado da filtragem:")
    for chave, valor in resultado.items():
        print(f"Chave: {chave} - Valor: {valor}")
else:
    print("Nenhum item corresponde ao filtro.")

print("\nDicionário original:")
for chave, valor in dicionario.items():
    print(f"Chave: {chave} - Valor: {valor}")