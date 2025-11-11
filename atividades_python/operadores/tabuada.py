# Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada 
 
""" x = int(input("Digite um número:"))
tabuada = [0,1,2,3,4,5,6,7,8,9,10]

for numeros in tabuada:
    print(x,"x",numeros,"=",x*numeros)"""

x = int(input("Digite um número:"))
tabuada = 0

while tabuada < 11:
    print(x,"x",tabuada,"=",x*tabuada)
    tabuada += 1
