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