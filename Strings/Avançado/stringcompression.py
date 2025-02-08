#Descrição: Programe um algoritmo que comprima uma string. Por exemplo, a string aaabbcc pode ser comprimida para a3b2c2.

print("Digite uma string para ser comprimida")
print("Exemplo: aaabbcc -> a3b2c2")
str_normal = str(input("Digite a String: "))
str_comprimida = ""
count = 0
i = 0

while i < len(str_normal):
    count = 1
    while i + 1 < len(str_normal) and str_normal[i] == str_normal[i + 1]:
        count += 1
        i += 1
    str_comprimida += str_normal[i] + str(count)
    i += 1

        
print("String comprimida:")
print(str_comprimida)