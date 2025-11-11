''' Faça um programa que leia um número inteiro e diga se ele é ou não
um número primo'''

numero = int(input('Digite um número inteiro: '))

divisores = 0  

for numeros  in range(1, numero + 1): 
    if numero % numeros == 0:  
        divisores += 1


if divisores == 2:
        print("O número é primo")
else:
        print("O número não é primo")

