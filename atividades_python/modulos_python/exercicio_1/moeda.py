'''Crie um módulo chamado moeda.py que tenha as funções incorporadas 'aumentar()', 
'diminuir()', 'dobro()' e 'metade()'.

Faça também um programa que importe esse módulo e use algumas dessas funções.

Obs.: por exemplo, o 'aumentar()' recebe o preço e uma porcentagem, e calcula,o 
'diminuir()', mesma coisa.'''


def aumentar(preco, porcentagem):
    return preco + (preco * porcentagem / 100)


def diminuir(preco, porcentagem):
    return preco - (preco * porcentagem / 100)


def dobro(preco):
    return preco * 2


def metade(preco):
    return preco / 2
