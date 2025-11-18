'''
Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os valores pares
e os valores ímpares digitados, respectivamente.

Ao final, mostre o conteúdo das três listas geradas.'''

numeros_digitados = []
lista_pares = []
lista_impares = []

while True:
    numeros = int(input("Digite um número inteiro: "))

    numeros_digitados.append(numeros)

    if numeros % 2 == 0:
        lista_pares.append(numeros)
    else:
        lista_impares.append(numeros)

    resposta_usuario = (input("Deseja continuar inserindo números? [S/N] ")).upper().strip()[0]

    if resposta_usuario == "S":
        continue
    elif resposta_usuario == "N":
       break
    else:
        print("Resposta inválida. Por favor, responda com 'S' ou 'N'.")
        continue

print("Números digitados:", numeros_digitados)
print("Números pares:", lista_pares)
print("Números ímpares:", lista_impares)