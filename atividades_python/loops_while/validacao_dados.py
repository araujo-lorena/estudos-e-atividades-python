'''
Faça um programa que leia o sexo de uma pessoa
mas só aceite os valores "M" ou "F".
Caso esteja errado, peça a digitação novamente
até ter um valor correto.
'''

sexo = input("Digite o seu sexo [M/F]:")

while sexo != "M" and sexo != "F":
    sexo = input("Dados inválidos. Por favor, digite o seu sexo [M/F]:")

print("Sexo",sexo, "registrado com sucesso.")
