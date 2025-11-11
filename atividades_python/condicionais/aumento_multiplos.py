"""
Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento
Para salários superiores a R$ 1.250,00, calcule um aumento de 10%
Para os inferiores ou iguais, o aumento é de R$ 15%.
"""

salario_atual_funcionario = float(input("Digite o salário atual do funcionário: R$ "))

if salario_atual_funcionario <= 1250:
    aumento = salario_atual_funcionario * 0.15
    novo_salario = salario_atual_funcionario + aumento
else:
    aumento = salario_atual_funcionario * 0.10
    novo_salario = salario_atual_funcionario + aumento

print("O aumento foi de :R$",aumento)
    
