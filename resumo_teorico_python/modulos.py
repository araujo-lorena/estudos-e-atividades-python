# Importação e criação de módulos em Python

"""
Em Python, um módulo é um arquivo que contém definições e instruções em Python. Ele pode definir 
funções, classes e variáveis, e também pode incluir código executável. Módulos permitem organizar
 o código em partes reutilizáveis e facilitam a manutenção e a legibilidade do código.Podemos criar
 nossos próprios módulos ou usar módulos pré-existentes da biblioteca padrão do Python
 ou de terceiros."""

#Importar modulos pré-existentes

"""Para importar um módulo em Python, usamos a palavra-chave 'import' seguida do nome do módulo.
 Por exemplo,para importar o módulo 'math', que fornece funções matemáticas, fazemos o seguinte:"""

import math
print(math.sqrt(16))  # Saída: 4.0
print(math.pi)        # Saída: 3.141592653589793


"""Também podemos importar apenas partes específicas de um módulo usando a palavra-chave 'from'."""

from math import factorial
print(factorial(5))  # Saída: 120

#Funções e classes de módulos padrão

"""A biblioteca padrão do Python inclui muitos módulos úteis. Aqui estão alguns exemplos de módulos
 comuns e suas funcionalidades: """

'''1.random: Gera números aleatórios e realiza operações relacionadas a aleatoriedade.
Exemplo:
'''
import random
print(random.randint(1, 10))  # Gera um número inteiro aleatório entre 1 e 10


'''2.datetime: Manipula datas e horas.
Exemplo:'''

import datetime
hoje = datetime.date.today()
print(hoje)  # Saída: Data atual


'''3.match: Trabalha com expressões regulares para busca e manipulação de strings.
Exemplo: '''

import re
padrao = r'\d+'
texto = "Há 2 gatos e 3 cachorros."
resultado = re.findall(padrao, texto)
print(resultado)  # Saída: ['2', '3']'''


#Criar módulos próprios/módulos personalizados

"""Para criar um módulo próprio, basta criar um arquivo Python (.py) com as definições de funções,
classes e variáveis que desejamos incluir no módulo. Por exemplo, podemos criar um arquivo chamado  
"meu_modulo.py" com o seguinte conteúdo.
Exemplo:"""

# meu_modulo.py

def saudacao(nome):
    return f"Olá, {nome}!"

def soma(a, b):
    return a + b


"""Depois de criar o módulo, podemos importá-lo em outro arquivo Python e usar suas funções.""" 

# main.py

#import meu_modulo as main_py
#print(main_py.saudacao("Maria"))  # Saída: Olá, Maria!
#print(main_py.soma(3, 5))          # Saída: 8


#Organização do código em módulos 

"""Organizar o código em módulos ajuda a manter o código limpo e facilita a reutilização. Aqui 
estão algumas dicas para organizar o código em módulos:

1. Agrupe funções e classes relacionadas em um mesmo módulo.
2. Use nomes descritivos para os módulos que reflitam seu conteúdo.
3. Mantenha os módulos pequenos e focados em uma única responsabilidade.
4. Documente as funções e classes dentro dos módulos para facilitar o entendimento.
5. Utilize pacotes (diretórios com um arquivo __init__.py) para organizar módulos relacionados em
 um namespace comum.
 Exemplo:"""

#operacoes/matematica.py

def adicionar(a, b):    
    return a + b

def subtrair(a, b):
    return a - b


#utilidades/texto.py

def contar_palavras(texto):
    palavras = texto.split()
    return len(palavras)

#operacoes/__init__.py
# Este arquivo pode estar vazio ou conter código de inicialização do pacote
# main.py

#from operacoes.matematica import adicionar, subtrair
print(adicionar(10, 5))  # Saída: 15
print(subtrair(10, 5))   # Saída: 5


#from utilidades.texto import contar_palavras
texto = "Olá mundo, este é um exemplo."
print(contar_palavras(texto))  # Saída: 6



#Pacotes em Python

"""Pacotes são uma forma de estruturar módulos em diretórios hierárquicos. Um pacote é simplesmente
 um diretório que contém um arquivo especial chamado __init__.py, que indica ao Python que aquele
 diretório deve ser tratado como um pacote. Pacotes permitem organizar módulos relacionados em
    um namespace comum, facilitando a importação e o gerenciamento do código."""

#Criar  e utilizar um pacote

"""Para criar um pacote, siga estes passos:
1. Crie um diretório com o nome do pacote.
2. Dentro desse diretório, crie um arquivo __init__.py (pode estar vazio ou conter código de
inicialização).
3. Adicione módulos (arquivos .py) dentro do diretório do pacote.
4. Importe os módulos do pacote em outros arquivos Python."""

# Estrutura do pacote:
# meu_pacote/
# ├── __init__.py
# ├── modulo1.py
# └── modulo2.py

# meu_pacote/modulo1.py
def funcao_modulo1():
    return "Função do módulo 1"

# meu_pacote/modulo2.py
def funcao_modulo2():
    return "Função do módulo 2"

