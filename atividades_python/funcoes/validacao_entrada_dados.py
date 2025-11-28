"""
Crie um programa que tenha a função leia_int(), 
que vai funcionar de forma semelhante à função input do Python,
só que fazendo a validação para aceitar apenas um valor numérico.

ex.:
n = leia_int("Digite um n")
"""

def leia_int():
    while True:
        valor = input("Digite um número inteiro: ")
        if valor.lstrip('-').valor.isdigit():
            return int(valor)
        else:
            print("Erro! Por favor, digite um número inteiro válido.")

numero = leia_int()
print(numero)