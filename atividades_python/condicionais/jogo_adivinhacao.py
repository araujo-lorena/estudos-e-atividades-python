"""
Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5
e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.

O programa deverá escrever na tela se o usuário venceu ou perdeu.

"""

numero = int(input("Escolha um número entre 0 e 5: "))
numero_escolhido_computador = 4

if numero == numero_escolhido_computador:
    print("Parabéns! Você venceu!")
else:
    print("Você perdeu! Tente novamente.")