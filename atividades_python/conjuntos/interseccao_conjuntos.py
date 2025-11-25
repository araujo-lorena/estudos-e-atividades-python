"""Dois professores têm listas de alunos que passaram em duas matérias diferentes.
Crie dois conjuntos com nomes dos alunos de cada matéria.
Mostre os alunos que passaram em ambas as matérias (interseção).
Mostre os alunos que passaram somente na primeira matéria.
Mostre os alunos que passaram somente na segunda matéria."""

ciberseguranca = {"Manuela","Alexia","Ava","Davi","Lorena","Esteban"}
robotica = {
    "Lorena","Esteban","Stela","Pietro","Augusto",
    "Manuela","Alexia","Ava","Arthur","Isabele",
    "Naxile","Sofia","Davi","Gabriel"
    }

aprovados_ciberseguranca_robotica = ciberseguranca & robotica
aprovados_somente_ciberseguranca = ciberseguranca - robotica
aprovados_somente_robotica = robotica - ciberseguranca

print("Alunos que passaram em ambas as matérias:", aprovados_ciberseguranca_robotica)
print("Alunos que passaram somente em Cibersegurança:", aprovados_somente_ciberseguranca)
print("Alunos que passaram somente em Robótica:", aprovados_somente_robotica)   