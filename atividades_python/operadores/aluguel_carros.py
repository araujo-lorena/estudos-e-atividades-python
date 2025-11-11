
""" Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de
 dias pelos quais ele foi alugado.Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e 
 R$ 0.15 por km rodado"""

quantidade_Km_percorridos = float(input("Qual foi a quantidade de Km percorridos pelo carro alugado? "))
quantidade_dias_alugados =int(input("Por quantos dias o carro foi alugado?"))

preco_aluguel_carro_dia_reais = 60.00
valor_Km_rodado_reais = 0.15

total_pagar = (quantidade_dias_alugados * preco_aluguel_carro_dia_reais) + (quantidade_Km_percorridos * valor_Km_rodado_reais)

print("O total pago foi de R$:",total_pagar)

