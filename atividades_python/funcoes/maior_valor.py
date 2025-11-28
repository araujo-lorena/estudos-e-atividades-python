"""
Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores 
inteiros.
Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
"""

def maior(*numeros):
    if len(numeros) == 0:
        return None
    
    maior_valor = numeros[0]

    for numero  in numeros:
        if numero > maior_valor:
            maior_valor = numero
    return maior_valor

print(maior(3, 7, 2, 9, 5))
