''' Faça um programa que leia um número qualquer e mostre
o seu fatorial 

exemplo: 5! = 5 * 4 * 3 * 2 * 1 = 120
'''

numero = int(input("Digite um número para calcular o fatorial: "))

resultado = 1
fatorial_numero = numero

while fatorial_numero > 0:
    resultado = resultado * fatorial_numero
    fatorial_numero -= 1

print("O fatorial do ",numero,"é:",resultado)