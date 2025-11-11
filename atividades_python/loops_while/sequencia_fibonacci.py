'''
Escreva um programa que leia um número n inteiro qualquer
e mostre na tela os primeiros n elementos e uma sequência de Fibonacci

1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584 (...)

'''

contador_fibonacci = 0

numero = int(input("Digite um número inteiro para ver a sequência de Fibonacci: "))
n_elementos = int(input("Quantos elementos da sequência de Fibonacci você quer ver? "))

while contador_fibonacci < n_elementos:
    calculo_fibonacci = numero + (numero - 1)
    contador_fibonacci += 1
    calculo_fibonacci += 1

print("A sequência de",n_elementos,"elementos para ", numero, "é:", calculo_fibonacci)


#Finalizar depois 

