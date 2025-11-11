# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto

preco_produto = float(input("Digite o preço do produto:R$"))
desconto_produto = preco_produto * 0.05
novo_preco_produto = preco_produto - desconto_produto

print("Preço Final:R$",novo_preco_produto)
