"""Faça um programa que calcule a soma entre todos os números impares
 que são múltiplos de três (3) e que se encontram no intervalo de 1 até 500."""

soma = 0
numeros = range(1, 501)
for numero in numeros:
    if numero % 2 != 0 and numero % 3 == 0:
        soma += numero
print("A soma dos números ímpares múltiplos de 3  de 1 até 500 é:", soma)