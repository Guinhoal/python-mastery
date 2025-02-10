#Descrição: Crie uma lista com 10 elementos e adicione os valores de 1 a 10.

list = []
print ("Digite membros de uma lista para ver o primeiro e o ultimo (caso não queira mais digitar, digite 'sair')")
while True:
    print("Digite o Item a ser adicionado: ")
    item = input()
    if item == "sair" or item == "SAIR" or item == "Sair":
        break
    else:
        list.append(item)

print("O primeiro item da lista é: ", list[0])
print("O ultimo item da lista é: ", list[-1])