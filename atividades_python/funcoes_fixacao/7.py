'''Função que repete uma palavra

Crie a função repetir(palavra, vezes) que imprime a palavra repetida o número de vezes indicado.'''

def repetir(palavra, vezes):
    for i in range(vezes):
        print(palavra)
print(repetir("Olá", 3))

def repetir(palavra, vezes):
    return palavra * vezes
print(repetir("Olá ", 3))
