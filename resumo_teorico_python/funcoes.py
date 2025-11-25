# FUNÇÕES

"""As funçoes são blocos de códigos reutilizáveis que nos permitem encapsular tarefas especifícas e executá
-las quando necessário.As funções nos ajudam a organizar nosso código,evitar repetição e fazer com que nos-
sos programas sejam mais modulares e fáceis de manter. """


# Definição e chamada de funcões

"""
def boas_vindas():
    print("Olá,sejam todos(as) bem-vindos(as) ao Rolê da nossa Universidade!")

boas_vindas()

"""

# Parâmetros e argumentos

"""def boas_vindas(curso):
    print("Olá,sejam todos(as) bem-vindos(as) a graduação de",curso,"!")

boas_vindas("Ciência da Computação")"""


# Valores de retorno

"""def divisao(x,y):
    return x / y

resultado = divisao(6,3)
print(resultado)"""

# Funções anônimas(lambda)

"""somar = lambda eu,voce: eu + voce
print(somar(1,1))"""


# Escopo das variáveis(local e global)

"""def funcao_exemplo1():
    variavel_local = "Eu sou uma variável local"
    print(variavel_local)

variavel_global = "Eu sou uma variável global"

def funcao_exemplo2():
 print(variavel_global)

funcao_exemplo1()
funcao_exemplo2()

print(variavel_global) # Isso funcionará, pois variavel_global é acessível globalmente
print(variavel_local)  # Isso gerará um erro, pois variavel_local não é acessível fora da função""" 


# Funções definidas pelo usuário 

"""
1. Documentação de funções(docstrings): Use docstrings para documentar suas funções.

2. Funções com número variável de argumentos: Use *args e **kwargs para permitir que suas funções
 aceitem um número variável de argumentos.
 
"""










