# Descrição: Faça um programa que leia uma frase e permita ao usuário escolher entre duas opções: colocar a frase 
# toda em maiúsculo ou em minúsculo. Exiba a frase alterada na tela. Se o usuário digitar uma opção inválida, exiba uma mensagem de erro.

print("Digite um frase:")
string_normal = str(input())
print("1 - Colocar tudo em maiúsculo")
print("2 - Colocar tudo em minúsculo")
opt = int(input("Selecione a opção desejada:"))
if opt == 1:
    string_alterada = string_normal.upper()
    print(string_alterada)
elif opt == 2:
    string_alterada = string_normal.lower()
    print(string_alterada)
else: 
    raise SyntaxError("Opção inválida")