"""Crie dois conjuntos com números aleatórios.
Faça a união dos conjuntos e mostre quantos elementos únicos existem no total.
Faça a diferença simétrica (elementos que estão em apenas um dos conjuntos)."""

primeiro_conjunto = {1,3,5,7,9}
segundo_conjunto = {2,4,6,8,10}

uniao = primeiro_conjunto | segundo_conjunto
diferenca_simetrica = primeiro_conjunto ^ segundo_conjunto

print("Conjunto 1:", primeiro_conjunto)
print("Conjunto 2:", segundo_conjunto)
print("União dos conjuntos:", uniao)
print("Diferença simétrica dos conjuntos:", diferenca_simetrica)
print("Número total de elementos únicos na união:", len(uniao))