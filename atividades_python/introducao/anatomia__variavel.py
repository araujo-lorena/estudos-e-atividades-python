""" Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações
 possíveis sobre ele"""

entrada = input("Digite algo: ")

print("Tipo primitivo: ", type(entrada))

print("É numérico? ",(entrada.isnumeric()))
print("É alfanumérico? ",(entrada.isalpha()))
print("É um decimal? ",(entrada.isdecimal()))
print("Está em caixa baixa? ",(entrada.islower()))
print("É apenas espaço em branco? ",(entrada.isspace()))
print("Está em caixa alta? ",(entrada.isupper()))