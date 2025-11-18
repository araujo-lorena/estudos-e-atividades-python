""" Crie um programa que tenha uma tupla com várias palavras
(não usar acentos).
Depois disso, você deve mostrar, para cada palavra,
quais são as suas vogais
"""

palavras = ('java','javascript','cobol','python','c++','c','c#','ruby','swift','kotlin')

for palavra in palavras:
    for letra in palavra:
        if letra in 'aeiou':
           # print('Na palvra',palavra,'tem(os) a(s) vogal(is):',letra)
            print("Na palavra", palavra, "tem(os) a(s) vogal(is):",",".join([letra for letra in palavra if letra in ['a','e','i','o','u']]))
           # print('Na palvra',palavra,'tem(os) a(s) vogal(is):',letra,)