""" Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média:mostre uma mensagem no
 final, de acordo com a média atingida:

- média abaixo de 5.0: reprovado
- média entre 5.0 e 6,9: recuperação
- média 7.0 ou superior: aprovado """

nota1 = float(input("Digite a primeiraa nota:"))
nota2 = float(input("Digite a segunda nota:"))

media_notas = (nota1 + nota2) / 2

print("Média de notas:", media_notas)

if media_notas < 5.0:
    print("Reprovado")
elif 5.0 <= media_notas <= 6.9:
    print("Recuperação")
else:   
    print("Aprovado")