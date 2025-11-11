''' Crie um programa que leia vários números inteiros pelo teclado
No final da execução, mostre a média entre todos os valores
e qual foi o maior e o menor valores lidos
O programa deve perguntar ao usuário se ele quer ou não continuar
a digitar valores
'''

soma = 0
maior_valor_lido = 0
menor_valor_lido = 0

while True:
    numeros = int(input("Digite um número inteiro:"))
    soma += numeros
    
    resposta_usuario = input("Quer continuar? [S/N]").upper().strip()

    if resposta_usuario == 'N':
        break
    else:
        continue

media = soma / numeros

print("Média:", media)
print("Maior valor lido:", maior_valor_lido)
print("Menor valor lido:", menor_valor_lido)

# Finalizar depois