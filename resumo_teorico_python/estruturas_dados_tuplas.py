#TUPLAS ()

"""Tuplas são estruturas de dados imutáveis em Python, usadas para armazenar
 múltiplos itens em uma única variável."""


#Criação e acesso

""" ponto = (22,65)

print(ponto[0])  
print(ponto[1]) """


#Metódos de tuplas

""" 1. count(elemento): Retorna o número de vezes que um valor específico aparece na tupla.
    2. index(elemento): Retorna o índice da primeira ocorrência de um valor específico.
    Opcionalmente, você pode fornecer índices de início e fim para limitar a busca.
    3. len(tupla): Retorna o número de elementos na tupla.
"""

numeros_pares = (2,4,6,8,10)

print(numeros_pares.count(4))  
print(numeros_pares.index(6))
print(len(numeros_pares))