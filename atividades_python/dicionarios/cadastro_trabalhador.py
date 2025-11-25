"""
Crie um programa que leia nome, ano de nascimento e carteira de trabalho
e cadastre-os (com idade) em um dicionário. 
Se por acaso a CTPS for diferente de zero, o dicionário receberá também
o ano de contratação e o salário.
Calcule e acrescente, além da idade, com quantos anos
a pessoa vai se aposentar.

Obs.: aposentadoria em 35 anos de contribuição.
"""

nome = (input("Nome: "))
ano_nascimento = int(input("Ano de nascimento: "))
carteira_trabalho = int(input("Carteira de Trabalho (0 não tem): "))

trabalhador = {"nome": nome,
                   "idade": 2025 - ano_nascimento,
                   "carteira_trabalho": carteira_trabalho
    }

if carteira_trabalho != 0:
         ano_contratacao = int(input("Ano de contratação: "))
         salario = float(input("Salário: R$ "))
         
         aposentadoria_idade = (ano_contratacao + 35) - ano_nascimento

         trabalhador.update({"ano_contratacao": ano_contratacao,
                            "salario": salario,
                            "aposentadoria_idade": aposentadoria_idade
         })

print([trabalhador])
         
resposta_usuario = input("Quer continuar? [S/N] ").strip().upper()
if resposta_usuario == "N":
      print("Encerrando o programa...")

          
