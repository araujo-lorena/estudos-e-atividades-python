'''
Crie um programa que tenha uma tupla única
com nomes de produtos e seus respectivos precos,
na sequência

No final, mostre uma listagem de precos,
organizando os dados em forma tabular
'''

produto_preco = (
    "Notebook", 25000.00,
    "Mouse", 150.00,
    "Teclado", 300.00,
    "Monitor", 1200.00,
    "Impressora", 800.00,
    "Cadeira", 450.00,
    "Mesa", 600.00,
    "Tripe", 200.00,
    "Camara", 500.00
     )

print("-" * 40)
print('LISTA DE PREÇOS:'.center(40))
print("-" * 40)

for i in range(0, len(produto_preco), 2):
    produto = produto_preco[i]
    preco = produto_preco[i + 1]
    print(f"{produto:.<30} R$ {preco:>7.2f}")

print("-" * 40)
                 