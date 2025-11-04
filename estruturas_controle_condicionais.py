# Estruturas de Controle 

"""As estruturas de controle nos permitem direcionar o fluxo de execução do código com 
base em condições específicas."""


#ESTRUTURAS CONDICIONAIS

# IF:

"""É a estrutura condicional mais simples. Ela executa um bloco de código se uma 
condição for verdadeira."""

#Ex:
"""idade = 22
if idade >= 18:
    print("Você é maior de idade.") """


# IF-ELSE:

"""É uma extensão da estrutura IF. Ela permite que um bloco de código alternativo seja
executado se a condição do IF for falsa."""

#Ex:
"""idade = 18
if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.") """


# IF-ELIF-ELSE:

"""É uma extensão da estrutura IF-ELSE. Ela permite verificar múltiplas condições,
executando o bloco de código correspondente à primeira condição verdadeira."""

#Ex:
""" idade = 22
if idade < 18:
    print("Você é menor de idade.")
elif idade == 18:
    print("Você acabou de se tornar maior de idade.")
else:
    print("Você é maior de idade.") """

