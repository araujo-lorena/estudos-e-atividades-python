"""Dada uma lista com números repetidos, transforme-a em um conjunto para eliminar duplicatas.
Converta novamente para lista e ordene os elementos."""

lista_duplicatas = [22, 11, 33, 22, 44, 11, 55, 33,17,56,99,88,106,106,45]
conjunto_sem_duplicatas = set(lista_duplicatas)
lista_sem_duplicatas = list(conjunto_sem_duplicatas)
lista_sem_duplicatas.sort()