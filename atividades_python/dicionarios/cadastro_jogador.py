"""
Crie um programa que gerencie o aproveitamento de um jogador de futebol.
O programa vai ler o nome do jogador e quantas partidas ele jogou.
Depois vai ler a quantidade de gols feitos em cada partida.
No final, tudo isso será guardado em um dicionário,
incluindo o total de gols feitos durante o campeonato.
"""

nome_jogador = input("Nome do jogador: ")
numero_partidas_jogadas = int(input("Quantas partidas " + nome_jogador + " jogou? "))
gols_por_partida = [] 

for partida in range(1, numero_partidas_jogadas + 1):
    gols = int(input("Quantos gols " + nome_jogador + " fez na partida ? "))
    gols_por_partida.append(gols)


estatisticas_jogador = {
    "nome_jogador": nome_jogador,
    "numero_partidas_jogadas": numero_partidas_jogadas,
    "gols_por_partida": gols_por_partida
    }

print(estatisticas_jogador)