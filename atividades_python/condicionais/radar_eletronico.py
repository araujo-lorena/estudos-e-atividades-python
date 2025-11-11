"""Escreva um programa que leia a velocidade de um carro
Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado
A multa vai custar R$7,00 por cada Km acima do limite.
"""

velocidade_carro_Km_h = float(input("Digite a velocidade do carro em Km/h: "))

if velocidade_carro_Km_h > 80:
    print("Você foi multado por excesso de velocidade!")

    multa = (velocidade_carro_Km_h - 80) * 7.00
    print("O valor da multa é de: R$", multa) 

