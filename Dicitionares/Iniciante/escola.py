print("Seja bem vindo ao sistema escolar")
print("Cadastre alunos e depois veja informações sobre eles")

print("Digite o nome da escola:")

nome = input()

def cria_escola():
    lista = []
    contador = 1
    while True:
        dicionario = {}
        print(f"Digite o nome do aluno {contador}:")
        nome = input()
        print(f"Digite a idade do aluno {contador}:")
        idade = int(input())
        print(f"Digite o curso do aluno {contador}")
        curso = input()
        dicionario["nome"] = nome
        dicionario["idade"] = idade
        dicionario["curso"] = curso
        lista.append(dicionario)
        print("Deseja continuar cadastrando ? (sim ou nao)")
        continuar = input()
        if continuar.lower() == "nao":
            break
        contador += 1
    return lista

alunos = cria_escola()

print("1 - Ver todos os alunos cadastrados")
print("2 - Buscar por aluno especifíco")

escolha = int(input())

def todos_alunos(alunos):
    contador = 1
    for aluno in alunos:
        print("-------------------------------------")
        print(f"Aluno - {contador}")
        print(f"Nome: {aluno["nome"]}")
        print(f"Idade: {aluno["idade"]}")
        print(f"Curso: {aluno["curso"]}")
        print("-------------------------------------")
        contador += 1

def buscar_alunos(alunos):
    print("Qual o nome do aluno que deseja buscar ?")
    name = input()
    for aluno in alunos:
        if name.lower() == aluno["nome"].lower():
            print("-------------------------------------")
            print(f"Nome: {aluno["nome"]}")
            print(f"Idade: {aluno["idade"]}")
            print(f"Curso: {aluno["curso"]}")
            print("-------------------------------------")
            break

while True:
    if escolha == 1:
        todos_alunos(alunos)
        break
    elif escolha == 2:
        buscar_alunos(alunos)
        break
    else:
        print("Opção Inválida")