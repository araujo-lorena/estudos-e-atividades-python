"""
Crie um programa que tenha uma função chamada voto()
que vai receber como parâmetro o ano de nascimento de uma pessoa, 
retornando um valor literal indicando se uma pessoa tem voto 
NEGADO, OPCIONAL ou OBRIGATORIO nas eleições.
"""

def voto(ano_nascimento):
    
    idade_pessoa = 2025 - ano_nascimento

    if idade_pessoa < 16:
        return "VOTO NEGADO"
    elif 18 <= idade_pessoa < 65:
        return "VOTO OBRIGATÓRIO"
    else:
        return "VOTO OPCIONAL"
    
ano = int(input("Digite o ano de nascimento: "))      
print(voto(ano))
