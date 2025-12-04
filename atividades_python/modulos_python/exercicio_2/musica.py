'''Enunciado:
Crie um módulo chamado musica.py que tenha as funções:

aumentar_volume() — recebe um valor de volume (0 a 100) e uma porcentagem para aumentar.

diminuir_volume() — recebe um valor de volume e uma porcentagem para diminuir.

dobrar_bpm() — recebe um valor de BPM (batidas por minuto) e devolve o dobro.

metade_bpm() — recebe um valor de BPM e devolve a metade.

Crie também um programa principal que importe esse módulo e use algumas dessas funções.

Obs.: As funções devem retornar os novos valores, não apenas imprimir.'''


def aumentar_volume(volume, porcentagem):
    return volume + (volume * porcentagem / 100)


def diminuir_volume(volume, porcentagem):
    return volume - (volume * porcentagem / 100)


def dobrar_bpm(bpm):
    return bpm * 2


def metade_bpm(bpm):
    return bpm / 2

