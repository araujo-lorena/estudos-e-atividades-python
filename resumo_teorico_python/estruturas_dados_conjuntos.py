# CONJUNTOS (set)

"""
Conjuntos são coleções não ordenadas e mutáveis de elementos únicos."""

#Criando e realizando operações básicas com conjuntos

#Criação

"""conjunto_a = {1, 2, 3, 4, 5}
   conjunto_b = set([4, 5, 6, 7, 8])
"""

#Operações

"""
1. União: conjunto_a | conjunto_b
2. Interseção: conjunto_a & conjunto_b
3. Diferença: conjunto_a - conjunto_b
4. Diferença simétrica: conjunto_a ^ conjunto_b
"""

#Ex:
"""conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = set([4, 5, 6, 7, 8])

uniao = conjunto_a | conjunto_b 
print(uniao)
intersecao = conjunto_a & conjunto_b
print(intersecao)
diferenca = conjunto_a - conjunto_b
print(diferenca)
diferenca_simetrica = conjunto_a ^ conjunto_b
print(diferenca_simetrica) """



#Métodos de conjuntos

"""
1. add(elemento): Adiciona um elemento ao conjunto.
2. remove(elemento): Remove um elemento do conjunto. Gera um erro se o elemento não
 existir.
3. discard(elemento): Remove um elemento do conjunto. Não faz nada se o elemento não
 existir.
4. clear(elemento): Remove todos os elementos do conjunto.
5. pop(): Remove e retorna um elemento arbitrário do conjunto.
"""

#Ex:
"""
carros = {"fusca", "gol", "celta"}

carros.add("palio")
print(carros)
carros.remove("gol")
print(carros)
carros.discard("santana")
print(carros)
carros.pop()
print(carros)
carros.clear() #set()
print(carros) """
