'''
Elabore um programa que calcule o valor a ser pago por um produto,
considerando o seu preço normal, e condição de pagamento:

1. à vista dinheiro/cheque: 10% de desconto
2. à vista no cartão: 5% de desconto
3. em até 2x no cartão: preço normal
4. em 3x ou mais no cartão: 20% de juros
'''

preco_produto = float(input("Digite o preço do produto: R$ "))

print("""Escolha a condição de pagamento:
[1] À vista dinheiro/cheque: 10% de desconto
[2] À vista no cartão: 5% de desconto
[3] Em até 2x no cartão: preço normal
[4] Em 3x ou mais no cartão: 20% de juros
""")

escolha_pagamento = int(input("Escolha a condição de pagamento:"))

if escolha_pagamento == 1:
    valor_pago =  preco_produto * 0.90
elif escolha_pagamento == 2:
    valor_pago = preco_produto * 0.95
elif escolha_pagamento == 3:
    valor_pago = preco_produto
elif escolha_pagamento == 4:
    valor_pago = preco_produto * 1.20
else:
    print("Opção inválida de pagamento.Tente novamente.")
    valor_pago = None
    
if valor_pago is not None:
 print("O valor a ser pago pelo produto é de :R$",valor_pago)
