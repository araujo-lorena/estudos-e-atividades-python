"""
1. Crie 2 listas:uma com 5 nomes(João,Maria,Cleber,Caio e Sarah) e outra com
5 valores em reais(R$) correspondentes ao saldo da conta do usuário(1350,20;
240,50;30,00;830,15 e 50,00),e usando laços de repetição, imprima os dados da 
seguinte forma(o preenchimento das listas deve ser feito também com laços de 
repetição do mesmo modo que será impresso:salvar nome e depois o saldo 
correspondente):

Entradas:
Insira o nome:****
Insira o saldo:****

...

Saída/Impressão:
LISTA DE CLIENTES - BANCO NACIONAL

NOME                 SALDO          CONTA
nome0                saldo0         #0
nome1                saldo1         #1
nome2                saldo2         #4 
 """ 


#Criando as listas

nomes = ["João","Maria", "Cleber", "Caio", "Sarah"]
saldos = [1350.20, 240.50, 30.00, 830.15, 50.00]
conta = [0,2, 4, 6, 8]


#Entrada de dados

informe_nome = input("Insira o nome:")
informe_saldo = float(input("Insira o saldo:")) 
informe_conta = int(input("Insira o número da conta:"))


#Saída

print("LISTA DE CLIENTES - BANCO NACIONAL")
print("NOME           SALDO          CONTA")

for informe_nome in nomes:
    for informe_saldo in saldos:
        for informe_conta in conta:
            print((informe_nome) ,(informe_saldo) ,(informe_conta))

# Finalizar depois
            