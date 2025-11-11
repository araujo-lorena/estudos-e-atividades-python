'''
Crie um programa onde o usuário possa digitar cinco valores numéricos
e cadastre-os em uma lista, já na posição correta de inserção
(sem usar o sort()).

No final, mostre a lista ordenada na tela.
'''

contador = 0
numeros_digitados = []

while contador < 5:
   numero = int(input('Digite um valor: '))
   contador += 1
   numeros_digitados += [numero]

   if numero > numeros_digitados[-1]:
      numeros_digitados.append(numero)
   else:
      numeros_digitados.insert(-2, numero)

print(numeros_digitados,",")

#Finalizar depois
