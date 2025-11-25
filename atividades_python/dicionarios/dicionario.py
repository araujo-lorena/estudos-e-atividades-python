"""
Faça um programa que leia nome e média de um aluno,
guardando também a situação em um dicionário.

No final, mostre o conteúdo da estrutura na tela.
"""

nome_aluno = input("Qual é o nome do aluno?")
media_aluno = input("Qual é a média do aluno?")

aluno = {"nome": nome_aluno, "media": media_aluno}

print(aluno["nome"], aluno["media"])
#print(aluno["media"])