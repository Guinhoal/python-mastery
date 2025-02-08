print("Digite uma string que deseja substituir as vogais por asteriscos: ")
str_normal = str(input())
str_normal = str_normal.lower()
print("Primeira forma")
str_final1 = ""
for letra in str_normal:
    if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
        str_final1 += "*"
    else:
        str_final1 += letra
print(str_final1)

print("Segunda forma")
str_final = str_normal.replace("a", "*").replace("e", "*").replace("i", "*").replace("o", "*").replace("u", "*")
print(str_final)