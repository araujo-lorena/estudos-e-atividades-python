# ARITMÉTICOS:

"""
Realizam operações matemáticas comuns, como adição, subtração, multiplicação e divisão.
"""

"""
1. Adição (+): Soma dois valores.
   Exemplo: resultado = 5 + 3   resultado será 8
   
   2. Subtração (-): Subtrai um valor de outro.
   Exemplo: resultado = 10 - 4   resultado será 6
   
   3. Multiplicação (*): Multiplica dois valores.
   Exemplo: resultado = 6 * 7   resultado será 42

   4. Divisão (/): Divide um valor por outro.
   Exemplo: resultado = 8 / 2   resultado será 4.0
   Obs: A divisão sempre retorna um float.

   5. Divisão inteira (//): Divide um valor por outro e retorna a parte inteira do resultado.
   Exemplo: resultado = 7 // 2   resultado será 3

   6. Módulo (%): Retorna o resto da divisão entre dois valores.
   Exemplo: resultado = 10 % 3   resultado será 1

   7. Exponenciação (**): Eleva um valor à potência de outro.
   Exemplo: resultado = 2 ** 3   resultado será 8 (2 elevado
   à potência de 3)
   """

# Exemplos de uso:

"""
a = 10
b = 3

soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
divisao_inteira = a // b
modulo = a % b
exponenciacao = a ** b

print("Soma:", soma)
print("Subtração:", subtracao)  
print("Multiplicação:", multiplicacao)
print("Divisão:", divisao)
print("Divisão Inteira:", divisao_inteira)
print("Módulo:", modulo)
print("Exponenciação:", exponenciacao)  
"""

# COMPARAÇÃO:

""" Realizam operações de comparação entre valores, retornando True ou False. """

"""
1. Igualdade (==): Verifica se dois valores são iguais.
   Exemplo: resultado = (5 == 5)   resultado será True

   2. Diferente de (!=): Verifica se dois valores são diferentes.
   Exemplo: resultado = (5 != 3)   resultado será True

   3. Maior que (>): Verifica se um valor é maior que outro.
   Exemplo: resultado = (5 > 3)   resultado será True

   4. Menor que (<): Verifica se um valor é menor que outro.
   Exemplo: resultado = (5 < 3)   resultado será False

   5. Maior ou igual a (>=): Verifica se um valor é maior ou igual a outro.
   Exemplo: resultado = (5 >= 5)   resultado será True

   6. Menor ou igual a (<=): Verifica se um valor é menor ou igual a outro.
   Exemplo: resultado = (5 <= 3)   resultado será False
   """

# Exemplos de uso:

"""
a = 10
b = 5

igualdade = (a == b)
diferente_de = (a != b)
maior_que = (a > b)
menor_que = (a < b)
maior_ou_igual = (a >= b)
menor_ou_igual = (a <= b)

print("Igualdade:", igualdade)
print("Desigualdade:", desigualdade)
print("Maior que:", maior_que)
print("Menor que:", menor_que)
print("Maior ou Igual:", maior_ou_igual)
print("Menor ou Igual:", menor_ou_igual)
"""

# LÓGICOS:

""" Realizam operações lógicas entre valores booleanos,combinando expressões condicionais,avaliando-as e 
 retornando True ou False. """

"""
1. E (and): Retorna True se ambos os operandos forem True.
   Exemplo: resultado = (5 > 3 and 8 > 5)   resultado será True

   2. Ou (or): Retorna True se pelo menos um dos operandos for True.
   Exemplo: resultado = (5 > 3 or 8 < 5)   resultado será True

   3. Não (not): Inverte o valor do operando.
   Exemplo: resultado = not (5 > 3)   resultado será False
   """  

# Exemplos de uso:  

"""
a = 10
b = 5

resultado_and = (a > 5 ) and (b < 10)
resultado_or = (a > 5) or (b > 10)
resultado_not = not (a > 5)

print("Resultado AND:", resultado_and)
print("Resultado OR:", resultado_or)
print("Resultado NOT:", resultado_not)
"""


# PRECEDÊNCIA DE OPERADORES:

"""

1. Parênteses: ( )
2. Exponenciação: **
3. Multiplicação e Divisão: *, /, //, %
4. Adição e Subtração: +, -
5. Comparação: <, >, <=, >=, ==, !=
6. Lógicos: and, or, not

"""