'''
A Confederação Nacional de Natação precisa de um programa que leia
o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:

- até 9 anos: mirim
- até 14 anos: infantil
- até 19 anos: júnior
- até 20 anos: sênior
acima de 20: master
'''

ano_nascimento = int(input("Digite o ano de nascimento do atleta: "))
ano_atual = 2025
idade = ano_atual - ano_nascimento

if idade <= 9:
    categoria = "Mirim"
elif idade <= 14:
    categoria = "Infantil"
elif idade <= 19:
    categoria = "Júnior"
elif idade <= 20:
    categoria = "Sênior"
else:
    categoria = "Master"
    
print("O atleta tem ",idade,"anos de idade e sua categoria é:",categoria)