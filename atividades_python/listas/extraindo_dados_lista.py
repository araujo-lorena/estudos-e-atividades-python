'''
Crie um programa que vai ler vários números e colocá-los em uma lista
Depois disso, mostre:
a) quantos números foram digitados.
b) a lista de valores, ordenada de forma decrescente
c) se o valor 5 foi digitado e está ou não na lista.
'''

numeros = []
qnt_numeros_digitados = 0

while True:
    numero = int(input("Digite um número:"))
    numeros.append(numero)

    qnt_numeros_digitados += 1
    numeros.sort(reverse=True)

    resposta_usuario = input("Deseja continuar? [S/N]").strip().upper()[0]
    if resposta_usuario == "N":
           break

print("Foram digitados",qnt_numeros_digitados,"números.")
print("Números em ordem decrescente:",numeros)

if 5 in numeros:
        print("O valor 5 foi digitado e está na lista.")
else:
        print("O valor 5 não foi digitado e não está na lista.")
