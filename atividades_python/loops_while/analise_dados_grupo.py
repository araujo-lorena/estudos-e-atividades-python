''' Crie um programa que leia a idade e o sexo de várias pessoas.
A cada pessoa cadastrada, o programa deverá perguntar
se o usuário quer ou não continuar.
No final, mostra:
a) quantas pessoas têm mais de 18 anos
b) quantos homens foram cadastrados
c) quantas mulheres têm menos de 20 anos'''

maior_18 = 0
homens_cadastrados = 0
mulheres_menos_20 = 0

while True:
    idade = int(input("Digite a idade da pessoa: "))
    sexo = int(input("Digite o sexo da pessoa [1-Masculino / 2-Feminino]: "))
    if sexo != 1 and sexo != 2:
        print("Opção inválida. Por favor, digite 1 para Masculino ou 2 para Feminino.")
        continue

    if idade >= 18:
      maior_18 += 1
    if sexo == 1:
       homens_cadastrados += 1
    if sexo == 2 and idade < 20:
       mulheres_menos_20 += 1
  
    resposta_usuario  = input("Deseja continuar cadastrando pessoas?")
    if resposta_usuario == 'sim':
        continue
    else:
        print("Cadastro finalizado.")
        break

print("Total de pessoas com mais de 18 anos: ",maior_18)
print("Total de homens cadastrados: ",homens_cadastrados)
print("Total de mulheres com menos de 20 anos: ",mulheres_menos_20)
