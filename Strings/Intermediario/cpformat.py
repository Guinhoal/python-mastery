# Descrição: Programa que recebe um CPF sem espaçamentos e imprime o CPF formatado.

print("Digite um número Cpf sem espaçamentos ou pontos/hifens")
str_normal = str(input())
cpf_formatado = ""
if str_normal.isdigit() and len(str_normal) == 11:
    for letra in range(len(str_normal)):
        if letra == 3 or letra == 6:
            cpf_formatado += "."
        elif letra == 9:
            cpf_formatado += "-"
        cpf_formatado += str_normal[letra]
    print("CPF formatado:")
    print(cpf_formatado)
else:
    print("Cpf inválido")