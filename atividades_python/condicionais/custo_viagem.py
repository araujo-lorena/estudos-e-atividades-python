"""
Desenvolva um programa que pergunte a distância de uma viagem em Km.
Calcule o preço da passagem, cobrando R$ 0,50 por Km para viagens de até 200km
e R$ 0,45 para viagens mais longas
"""

distancia_viagem_Km = float(input("Digite a distância da viagem em Km: "))

preco_passagem_ate_200Km = 0.50
preco_passagem_maior_200Km = 0.45   

if distancia_viagem_Km <= 200:
        preco = distancia_viagem_Km * preco_passagem_ate_200Km
else:
        preco = distancia_viagem_Km * preco_passagem_maior_200Km

print("O preço da passagem é de: R$", preco)