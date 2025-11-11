# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento

salario_atual_funcionario = float(input("Digite o salário atual do funcionário: R$ "))
reajuste_salarial_funcionario = salario_atual_funcionario * 0.15
novo_salario_funcionario = salario_atual_funcionario +reajuste_salarial_funcionario

print("O valor do salário do funcionário após o reajuste é de :R$",novo_salario_funcionario)