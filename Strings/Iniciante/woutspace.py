print("Digite a string que deseja ver sem espaços no começo e no fim: ")
string_usada = str(input())
print(f"String digitada: {string_usada}")
new_string = string_usada.strip()
print(f"String sem espaços no inicio e no fim: {new_string}")     