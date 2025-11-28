"""
Faça um programa que tenha uma função notas()
que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:

a quantidade de notas
a maior nota
a menor nota
a média da turma
a situação (opcional)

Adicione também as docstrings da função
"""

#Criando a função notas

def nota(*notas):
  notas_alunos = {}

# Preenchendo o dicionário com as informações solicitadas

  notas_alunos["quantidade_notas"] = len(notas)
  notas_alunos["maior_nota"] = max(notas)
  notas_alunos["menor_nota"] = min(notas)
  notas_alunos["media_turma"] = sum(notas) / len(notas)

# Verificando a situação da turma com base na média

  if notas_alunos["media_turma"] >= 7:
        notas_alunos["situacao"] = "Aprovado"
  elif 5 <= notas_alunos["media_turma"] < 7:
        notas_alunos["situacao"] = "Recuperação"
  else:
        notas_alunos["situacao"] = "Reprovado"
  
  return notas_alunos
  
# Testando a função notas
        
notas_alunos = nota(8, 6, 9, 5, 7,2,3,0,1,10,7,8)
print(notas_alunos)

