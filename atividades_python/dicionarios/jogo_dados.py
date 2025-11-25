"""
Crie um programa onde 4 jogadores joguem um dado
e tenham resultados aleatórios.
Guarde esses resultados em um dicionário.

No final, coloque esse dicionário em ordem,
sabendo que o vencedor tirou o maior número no dado
"""

jogadores = {}
valores_ordenados = []

for jogador in range(1,5):
    lado_dado = int(input("Qual lado do dado você tirou? "))
    jogadores[jogador] = lado_dado
    valores_ordenados.append(lado_dado)
    
valores_ordenados.sort(reverse=True)

print("Valores dos dados em ordem decrescente:", valores_ordenados,", onde o maior valor é o vencedor.")