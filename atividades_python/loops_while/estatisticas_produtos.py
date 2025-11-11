'''Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar.
No final, mostre:
a) qual é o total gasto na compra
b) quantos produtos custam mais de R$ 1000
c) qual é o nome do produto mais barato
'''

total_gasto_compra = 0
qtd_produtos_mais_1000 = 0
nome_produto_mais_barato = ''
preco_produto_mais_barato = 0


while True:
    nome_produto = input("Digite o nome do produto: ")
    preco_produto = float(input("Digite o preço do produto: R$ "))
   
    total_gasto_compra += preco_produto
    if preco_produto > 1000:
     qtd_produtos_mais_1000 += 1

    resposta_usuario = input("Deseja continuar? [S/N]: ").strip().upper()

    if resposta_usuario == "N":
        break
    else:
        continue

print("Total gasto na compra:", total_gasto_compra)
print("Quantidade de produtos acima de R$ 1000:", qtd_produtos_mais_1000)
print("Produto mais barato:", nome_produto_mais_barato, "por R$", preco_produto_mais_barato)

# Finalizar depois