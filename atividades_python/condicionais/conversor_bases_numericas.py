''' Escreva um programa que leia um número inteiro qualquer
e peça para o usuário escolher qual será a base de conversão:
1 para binário
2 para octal
2 para hexadecimal
'''

numero_inteiro = int(input('Digite um número inteiro: '))
base_conversao = int(input('Escolha a base de conversão:'))
                           

if base_conversao == 1:
 conversao_numero = "Binário"
elif base_conversao == 2:
  conversao_numero = "Octal"
else:
  conversao_numero = "Hexadecimal"

print("O número digitado foi:",numero_inteiro,"e a escolha da base de conversão foi:", conversao_numero)


                     
