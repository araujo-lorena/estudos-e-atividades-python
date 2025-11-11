# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros
#1 metro = 100 centímetros
#1 metro = 1000 milímetros

valor_metros = float(input("Digite o valor em metros:"))
conversao_metro_centimetro = valor_metros * 100
conversao_metro_milimetro = valor_metros * 1000 

print (valor_metros,"metros equivale a ",conversao_metro_centimetro,"centímetros e ",conversao_metro_milimetro,
       "milimetros.")
