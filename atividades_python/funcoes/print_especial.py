"""Faça um programa que tenha uma função chamada escreva(), 
que receba um texto qualquer como parâmetro 
e mostre uma mensagem com tamanho adaptável.

Ex:
escreva("Olá, Mundo!")

Saída:

~~~~~~~~~~~
Olá, Mundo!
~~~~~~~~~~~
"""

def escreva(hobbies):
    tamanho = len(hobbies) + 4
    print("-" * tamanho)
    print(hobbies)
    print("-" * tamanho)

escreva("Ler livros,Escutar música e podcasts,Viajar,Dormir,Comer,Cozinhar,Academia,Programar,"
"Assistir séries e filmes")    



