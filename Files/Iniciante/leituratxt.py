import os
import json
import csv

caminho_arquivo = "python-mastery/Files/examples/textos/texto1.txt"

if os.path.exists(caminho_arquivo):
    print("O arquivo existe")
else:
    print("O arquivo não existe")

with open(caminho_arquivo, "r", encoding='utf-8') as f :
    conteudo = f.read()
    print("Arquivo printado a partir do conteúdo completo:")
    print(conteudo)

    f.seek(0)

    print("Arquivo printado linha por linha:")
    linhas = f.readlines()
    numero_linhas = len(linhas)
    print(f"O arquivo possui {numero_linhas}")
    print("Arquivo completo:")
    print(linhas)
    f.close()