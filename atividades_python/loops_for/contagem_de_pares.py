# Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50

numeros = range(1, 51)
for numeros_pares in numeros:
    if numeros_pares % 2 == 0:
        print("Pares:",numeros_pares)
