# Entradas e Saídas em Python

"""Em Python, a entrada e saída de dados são realizadas principalmente através das funções
built-in input() e print(). Essas funções permitem interagir com o usuário, recebendo dados 
e exibindo informações no console."""

# Entrada de Dados do Usuário

"""A função input() é usada para capturar dados fornecidos pelo usuário durante a execução
do programa. Ela exibe uma mensagem opcional para o usuário e aguarda a entrada de dados.

Exemplo:

nome = input("Digite seu nome: ")
print("Olá, " + nome + "!")


Obs: A função input() sempre retorna uma string. Se você precisar de outro tipo de dado,
como um número inteiro ou um número de ponto flutuante, será necessário converter a string
 usando funções como int() ou float().  

Exemplo de conversão:

idade = int(input("Digite sua idade: "))
print("Você tem " + str(idade) + " anos.")
print("Ocorreu um erro inesperado:", e)
""" 

# Saída de Dados para o Usuário

"""A função print() é usada para exibir informações no console. Ela pode imprimir strings,
números e outros tipos de dados, separados por vírgulas.

Exemplo:

print("Olá, " + nome + "! Você tem " + str(idade) + " anos.")

# Você também pode usar formatação de strings para melhorar a saída:
print(f"Olá, {nome}! Você tem {idade} anos.")

# Ou usar o método format():
print("Olá, {}! Você tem {} anos.".format(nome, idade))
"""


# Leitura e Escrita de Arquivos

"""Python também oferece suporte para leitura e escrita de arquivos através das funções
open(), read(), write() e close()."""



# Abrindo um arquivo para escrita

"""Para ler o conteúdo de um arquivo,primeiro abra-o no modo de leitura utilizando o modo "r".
Depois, use o método read()  ou readline() para ler o conteúdo do arquivo. Finalmente, feche o
 arquivo usando o método close().

Exemplo:

arquivo = open("exemplo.txt", "r")
conteudo = arquivo.read()
print(conteudo)
arquivo.close()
"""

# Escrita de arquivo

"""Para escrever dados em um arquivo, abra-o no modo de escrita ("w") utilizando a função open().
Se o arquivo não existir, ele será  criado automaticamente. Se já existir, seu conteúdo será
sobrescrito.

Exemplo:

arquivo = open("exemplo.txt", "w")
arquivo.write("Olá, mundo!\n")
arquivo.write("Esta é uma linha escrita em um arquivo.\n")
arquivo.close()
"""

#  With

"""Uma maneira mais segura e conveniente de trabalhar com arquivos em Python é usar a
declaração with. Isso garante que o arquivo seja fechado corretamente, mesmo que ocorra um
  erro durante a operação de leitura ou escrita.

Exemplo:

with open("exemplo.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)
    
""" 