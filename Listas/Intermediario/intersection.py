#Descrição: Faça um programa que leia duas listas de números e retorne uma lista com os números 
# que estão presentes em ambas as listas.

lista1 = []
lista2 = []
numero = None
print("Insira elementos em 2 listas diferentes para ser verificado se as listas possuem elementos em comum")
print("Insira os elementos da primeira lista, caso queira parar digite 'sair'")
while True:
    print("Digite o elemento: ")
    numero = input()
    if numero == "sair" or numero == "SAIR" or numero == "Sair":
        break
    else:
        lista1.append(numero)

numero = None

print("Insira os elementos da segunda lista, caso queira parar digite 'sair'")
while True:
    print("Digite o elemento: ")
    numero = input()
    if numero == "sair" or numero == "SAIR" or numero == "Sair":
        break
    else:
        lista2.append(numero)

print("Primeira forma")

sem_duplicadas1 = set(lista1)
sem_duplicadas2 = set(lista2)

intersection_1 = sem_duplicadas1.intersection(sem_duplicadas2)

print(intersection_1)

intersection_2 = []

print("Segunda Forma")

if len(lista1) >= len(lista2):
    for num1 in lista1:
        for num2 in lista2:
            if num2 == num1 and num1 not in intersection_2:
                intersection_2.append(num1)
else:
    for num2 in lista2:
        for num1 in lista1:
            if num1 == num2 and num1 not in intersection_2:
                intersection_2.append(num2)

print(intersection_2)