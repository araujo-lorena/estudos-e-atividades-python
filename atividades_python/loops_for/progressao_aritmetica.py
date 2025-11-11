''' Desenvolva um programa que leia o primeiro termo e a razão
de uma PA (Progressão Aritmética).
No final, mostre os 10 primeiros termos dessa progressão.'''

primeiro_termo = int(input("Digite o primeiro termo da PA: "))
razao = int(input("Digite a razão da PA: "))

for termo in range(10):
    print(primeiro_termo + (termo * razao))