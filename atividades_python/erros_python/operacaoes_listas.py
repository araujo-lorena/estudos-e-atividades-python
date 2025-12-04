"""Escreva um programa que acesse um índice de uma lista que está fora do intervalo. Capture a
 IndexError e avise o usuário."""

def acessar_indice(lista, indice):
    try:
        print( lista[indice] )
        return lista[indice]
    
    except IndexError:
        print(f"Erro: O índice {indice} está fora do intervalo da lista.")
    
acessar_indice(["alho", "cebola", "maracujá"], 1)
    
