'''
Crie um programa que leia vários números inteiros pelo teclado
O programa só vai parar quando o usuário digitar o valor 999,
que é a condição de parada

No final, mostre quantos números foram digitados e qual foi a soma
entre eles (desconsiderando o flag!)
'''

soma = 0
qtd_numeros_digitados = 0

numero = int(input("Digite um número inteiro (999 para parar): "))

while numero != 999:
    soma = soma + numero
    qtd_numeros_digitados += 1
    numero = int(input("Digite um número inteiro (999 para parar): "))

print("Programa finalizado!")
print("Quantidade de números digitados:", qtd_numeros_digitados, "Soma dos números:", soma)
      