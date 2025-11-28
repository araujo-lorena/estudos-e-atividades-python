"""Faça um programa que tenha uma função chamada area(), que receba dimensões de um terreno
 retangular (largura e comprimento) e mostre a área do terreno
"""

def area(largura, comprimento):
    return largura * comprimento

largura = float(input("Digite a largura do terreno em metros: "))
comprimento = float(input("Digite o comprimento do terreno em metros: "))
area_terreno = area(largura, comprimento)

print("A área do terreno de",largura,"m x",comprimento,"m é de",area_terreno,"m².")
