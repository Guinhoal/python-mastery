print("Digite o código que deseja expandir para uma string")
print("Exemplo: a3b2c2 -> aaabbcc")
str_normal = str(input("Digite o Código: "))
str_exandida = ""

for i in range(0, len(str_normal), 2):
    str_exandida += str_normal[i] * int(str_normal[i + 1])
    
print("String expandida:")
print(str_exandida)