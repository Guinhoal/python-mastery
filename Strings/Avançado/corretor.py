#Descrição: Corretor de frases com abreviações de palavras

print("Digite um frase com abreviação de palvaras (Ex: vc, tbm, pq)")
print("Exemplo: vc tbm pq -> você também porque")
string_normal = str(input())
list_strigs = string_normal.split(" ")

for i in list_strigs:
    if i == "vc":
        list_strigs[list_strigs.index(i)] = "você"
    if i == "tbm":
        list_strigs[list_strigs.index(i)] = "também"
    if i == "pq":
        list_strigs[list_strigs.index(i)] = "porque"

string_alterada = " ".join(list_strigs)
print("String sem abreviações:")
print(string_alterada)