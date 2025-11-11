""" Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de
 tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m²"""

largura_parede = float(input("Digite a largura da parede em metros:"))
altura_parede = float(input("Digite a altura da parede em metros:"))

area_parede = largura_parede * altura_parede
quantidade_tinta_necessaria = area_parede / 2

print("A quantidade de tinta necessária para pintar essa parede é de :",quantidade_tinta_necessaria,
"litros")