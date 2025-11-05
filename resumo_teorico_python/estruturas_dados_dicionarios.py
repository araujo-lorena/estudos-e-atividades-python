#DICIONÁRIOS {}

"""
Dicionários são estruturas de dados que armazenam pares de chave-valor. Eles são
mutáveis e ordenados, o que significa que você pode alterar seu conteúdo após a criação.
As chaves devem ser únicas e imutáveis (como strings, números ou tuplas), enquanto os 
valores podem ser de qualquer tipo."""


#Criando e acessando dicionários

""" treino_musculacao = {"segunda-feira":"membros inferiores completo e cardio na bicicleta",
                     "terça-feira":"costas completo e cardio na escada",
                     "quarta-feira":"peito completo e cardio na esteira",
                     "quinta-feira":"membros inferiores completo e cardio na bicicleta",
                     "sexta-feira":"costas completo e cardio na escada"}

print(treino_musculacao["segunda-feira"])
print(treino_musculacao["terça-feira"])
print(treino_musculacao["quarta-feira"])
print(treino_musculacao["quinta-feira"])
print(treino_musculacao["sexta-feira"]) """


#Acessando com o get()

"""Semelhante ao acesso direto, mas retorna None (ou um valor padrão especificado) se a
chave não existir."""

carro = {"marca":"Toyota", "modelo":"Audi", "ano":2020}

print(carro.get("marca"))
print(carro.get("modelo"))
print(carro.get("ano"))
print(carro.get("cor","Preto"))


#Metódos de dicionários

"""
1. keys(): Retorna uma visualização de todas as chaves do dicionário.
2. values(): Retorna uma visualização de todos os valores do dicionário.
3. items(): Retorna uma visualização de todos os pares (chave, valor) do dicionário.
4. pop(chave): Remove e retorna o valor associado à chave especificada.
5. update(outro_dicionario): Atualiza o dicionário com os pares chave-valor de outro
 dicionário.
"""

#Ex: 

""" universitaria = {"nome":"Nexus", "idade":20, "curso":"Medicina"}

    print(universitaria.keys())
    print(universitaria.values())
    print(universitaria.items())
    universitaria.update({"ano":"2º"})
    print(universitaria) """