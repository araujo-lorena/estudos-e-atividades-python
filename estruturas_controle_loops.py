# LOOPS

"""Nos permitem repetir trechos de código diversas vezes, facilitando tarefas repetitivas,
 com base em condições específicas."""


# FOR:

"""É usado para iterar sobre uma sequência (como listas, tuplas, dicionários, conjuntos ou
 strings)"""

# Ex:
"""frutas = ["maçã", "banana", "cereja"]
for fruta in frutas:
    print(fruta)"""


# WHILE:

"""É usado para executar um bloco de código enquanto uma condição for verdadeira."""

# Ex:
"""contador = 1
while contador <= 5:
    print("Contador:", contador)
    contador += 1 """

#CONTROLE DE LOOPS

"""Podemos controlar o fluxo de execução dentro dos loops usando algumas instruções
 especiais."""


# BREAK:
"""É usado para interromper a execução de um loop prematuramente,independentemente da 
condição."""

# Ex:
"""contador = 1
while contador <= 5:
    if contador == 3:
        break
    print("Contador:", contador)
    contador += 1"""


#CONTINUE:
"""É usado para pular a iteração atual de um loop e continuar com a próxima."""

# Ex:
"""contador = 1
while contador <= 5:
    if contador == 3:
        continue
    print("Contador:", contador)
    contador += 1"""
    


#PASS:
"""É uma instrução nula que é usada quando uma declaração é sintaticamente necessária,
 mas nenhuma ação é desejada.Pode ser útil quando você está escrevendo código e ainda não
 decidiu o que fazer em um determinado bloco."""

#Ex:

"""for letra in "Python":
    if letra == "h":
        pass  # Não faz nada quando a letra é 'h'
    else:
        print("Letra:", letra)"""


#OBS:

#Iterar: Significa percorrer cada item de uma coleção de dados, como uma lista ou uma string







