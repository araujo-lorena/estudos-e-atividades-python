# Tratamento de Erros e Exceções em Python

"""
Em Python, o tratamento de erros e exceções é feito principalmente através das estruturas try, 
except, else e finally. Essas estruturas permitem que você lide com situações inesperadas
de forma controlada, evitando que o programa termine abruptamente.
Quando ocorre um erro,Python gera uma exceção e exibe uma mensagem de erro que inclui
o tipo da exceção e uma descrição do problema."""


# Erros comuns em Python incluem:

"""
1. SyntaxError: Erro de sintaxe no código.
2. TypeError: Ocorre se realiza uma operação em um tipo de dados imcompatível,como somar 
uma string com um número.
3. ValueError: Função recebe um argumento com o tipo correto, mas valor inapropriado.
4. IndexError: Índice fora do intervalo em listas ou tuplas.
5. KeyError: Chave inexistente em um dicionário.
6. ZeroDivisionError: Tentativa de divisão por zero.
7. FileNotFoundError: Tentativa de abrir um arquivo que não existe.
8. ImportError: Falha ao importar um módulo.
9. AttributeError: Tentativa de acessar um atributo inexistente em um objeto.
10. NameError: Tentativa de usar uma variável que não foi definida.
"""

# Manejo de Exceções

"""O manejo de exceções nos permite capturar e tratar erros de maneira controlada utilizando
as palavras-chave try, except, else e finally."""


#TRY 

"""A estrutura básica para capturar exceções é o bloco try-except. O código que pode gerar
uma exceção é colocado dentro do bloco try, e o código para tratar a exceção é colocado
dentro do bloco except.

Exemplo:

try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("Erro: Divisão por zero não é permitida.")
"""

# EXCEPT

"""O bloco except pode capturar exceções específicas ou todas as exceções genéricas.

Exemplo:

try:
    numero = int(input("Digite um número: "))
    resultado = 10 / numero
except ValueError:
    print("Erro: Entrada inválida. Por favor, digite um número inteiro.")
except ZeroDivisionError:
    print("Erro: Divisão por zero não é permitida.")
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")
    """

# ELSE

"""O bloco else é opcional e é executado se o código dentro do bloco try não gerar
nenhuma exceção.

Exemplo:

try:
    numero = int(input("Digite um número: "))
    resultado = 10 / numero
except ZeroDivisionError:
    print("Erro: Divisão por zero não é permitida.")
else:
    print(f"O resultado é: {resultado}")    
"""

# FINALLY

"""O bloco finally é opcional e é sempre executado, independentemente de uma exceção
ter sido gerada ou não. É útil para liberar recursos, como fechar arquivos ou conexões
de rede.

Exemplo:

try:
    arquivo = open("dados.txt", "r")
    conteudo = arquivo.read()
except FileNotFoundError:
    print("Erro: Arquivo não encontrado.")
finally:
    arquivo.close()
    print("Arquivo fechado.")     
"""


# Exceções Personalizadas

"""Você também pode criar suas próprias exceções personalizadas definindo uma nova classe
que herda da classe Exception. Isso é útil quando você deseja representar erros específicos
em seu aplicativo. 

Exemplo:

class MinhaExcecaoPersonalizada(Exception):
    pass
try:
    raise MinhaExcecaoPersonalizada("Esta é uma exceção personalizada.")
except MinhaExcecaoPersonalizada as e:
    print(e)
    
"""