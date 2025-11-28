'''Função que retorna o maior número

Crie a função maior(a, b) que devolve o maior dos dois números.'''


def maior(a,b):
    if a > b:
        return a
    else:
        return b
print(maior(9,5))


def maior(a,b):
    return max(a,b)
print(maior(3,7))