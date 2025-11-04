#ESTRUTURAS DE DADOS

"""As estruturas de dados nos permitem organizar e manipular dados de forma eficiente em
 Python.Aqui estão algumas das estruturas de dados mais comuns em Python:lista, tuplas,
   conjuntos e dicionário."""



#LISTA []

"""Listas são coleções ordenadas e mutáveis de itens. Elas podem conter elementos de 
diferentes tipos."""

#Criando e acessando uma lista

""" cores_favoritas = ["preto","roxo","azul","verde"]

print(cores_favoritas[0])
print(cores_favoritas[1])
print(cores_favoritas[2])
print(cores_favoritas[3]) """

#Acessando elementos negativos(ordem reversa)

""" print(cores_favoritas[-1]) #Acessa o último elemento
print(cores_favoritas[-2])
print(cores_favoritas[-3])
print(cores_favoritas[-4])  """


#Metódos de listas

"""As listas possuem diversos métodos embutidos que facilitam a manipulação e modificação
 dos dados.Alguns dos métodos mais comuns incluem :

   1. append(elemento)=> Adiciona um elemento ao final da lista.
   2. insert(indice, elemento)=> Adiciona um elemento em uma posição específica.
   3. remove(elemento)=> Remove a primeira ocorrência de um elemento.
   4. pop(indice)=> Remove e retorna o elemento na posição especificada.
   5. sort()=> Ordena os elementos da lista.
   6. reverse()=> Inverte a ordem dos elementos da lista.  """


"""series = ["Wandinha","La Casa de Papel","Stranger Things","Dark","Game of Thrones",
          "Vikings"]

series.append("Blindspot") 
print(series)
series.insert(3,"Breaking Bad")
print(series)
series.remove("Vikings")  
print(series)
serie_removida = series.pop(4) #Dúvida:tem como aplicar sem criar outra variável?Sim
print(series)
print("Série removida:", serie_removida)
series.sort()  #
print(series)
series.reverse() 
print(series) """



#Lista de compreensão

"""Listas de compreensão são uma maneira concisa de criar listas com base em uma sequência 
existente.Permitem filtrar e transformar elementos de uma lista em uma única linha de 
código."""

numeros =[1,2,3,4,5,6,7,8,9,10]
impares = [numero for numero in numeros if numero % 2 != 0]
print(impares)  
