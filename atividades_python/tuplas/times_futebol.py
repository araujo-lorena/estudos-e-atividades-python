'''
Crie uma tupla preenchida com os 20 primeiros colocados
da Tabela do Campeonato Brasileiro,
na ordem de colocação.
Depois mostre:
a) apenas os 5 primeiros colocados
b) os últimos 4 colocados da tabela
c) uma lista com os times em ordem alfabética
d) em que posição na tabela está o time do Cruzeiro
'''

times_brasileirao = ("Flamengo", "Palmeiras", "Cruzeiro", "Mirassol", "Botafogo", "Bahia",
    "São Paulo", "Fluminense", "Red Bull Bragantino", "Grêmio",
    "Vasco da Gama", "Corinthians", "Ceará", "Atlético-MG", "Internacional",
    "Santos", "Juventude", "Vitória", "Fortaleza", "Sport")

print("a) Os 5  primeiros colocados são:",times_brasileirao[0:5])
print("b) Os últimos 4 colocados são:",times_brasileirao[-4:])
print("c) Times em ordem alfabética:",sorted(times_brasileirao))
print("d) O Cruzeiro está na",times_brasileirao.index("Cruzeiro")+1,"ª posição")
