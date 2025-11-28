'''Função que verifica se o número é par

Crie a função eh_par(n) que retorna True se o número for par e False caso contrário'''

def eh_par(n):
    if n % 2 == 0:
        return True
    else:
        return False
print(eh_par(1))