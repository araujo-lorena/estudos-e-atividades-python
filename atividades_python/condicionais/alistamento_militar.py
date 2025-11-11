'''
Faça um programa que leia o ano de nascimento de um jovem e informe
de acordo com sua idade:

- Se ele ainda vai se alistar ao serviço militar
- Se é a hora de se alistar
- Se já passou do tempo do alistamento

Seu programa também deverá mostrar o tempo que faltou ou que passou do prazo
'''

ano_nascimento = int(input("Digite o ano de nascimento: "))

ano_atual = 2025
idade = ano_atual - ano_nascimento

idade_minima = 18
idade_maxima = 45


if idade <idade_minima :
    tempo = idade_minima - idade
    print("Você não possui idade suficiente para se alistar.Ainda faltam",tempo,"anos")
elif idade >= idade_minima and idade <= idade_maxima:
    tempo = idade - idade_minima
    print("Está na hora de se alistar ao serviço militar.Já passaram ",tempo,"anos")
else:
    tempo = idade - idade_maxima
    print("Você já passou do tempo de alistamento.Já se passaram",tempo,"anos                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       ")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      