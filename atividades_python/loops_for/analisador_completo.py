''' Desenvolva um programa que leia nome, idade e sexo de 4 pessoas
No final do programa, mostre:
 - A média de idade do grupo
 - Qual é o nome do homem mais velho
 - Quantas mulheres têm menos de 20 anos
 '''

contador = 0
media_idade = 0
mulheres_menos_20 = 0
nome_homem_mais_velho = ''
idade_homem_mais_velho = 0

while contador < 4:
    nome = input('Digite o nome: ')
    idade = int(input('Digite a idade: '))
    sexo = input('Digite o sexo [M/F]: ').strip().upper() 

    contador += 1
    idade_homem_mais_velho = idade
   

    if sexo == 'F' and idade < 20:
     mulheres_menos_20 += 1

    if sexo == "M":
     if idade_homem_mais_velho > idade:
        nome_homem_mais_velho = nome

media_idade += idade
media_idade = media_idade / 4

print('Média de idade do grupo:',media_idade )
print('Quantidade de mulheres com menos de 20 anos:', mulheres_menos_20)
print('Nome do homem mais velho:', nome_homem_mais_velho)

# Finalizar depois