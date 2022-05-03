'''Os professores de Educação Física estão organizando uma seletiva para montar a equipe de
natação. Para isso, eles convocaram os 7 melhores tempos da última competição e marcaram o tempo
de cada um dos nadadores, na prova dos 25 metros, estilo livre. Considerando que não houve tempos
iguais, construa um programa que leia o nome e o tempo (em segundos) de cada atleta e, em seguida,
gere o seguinte relatório: a) nome do nadador com o melhor tempo. b) nome do nadador com o pior
desempenho. c) tempo médio dos nadadores e d) quantidade de atletas com o tempo entre 12s e 15s.'''

soma = 0

nome = input('Nadador 1: ')
tempo = float(input('Tempo do nadador 1: '))

melhornadador = nome
melhortempo = tempo
piornadador = nome
piortempo = tempo

somatempo = 0
soma += tempo
tempo12s15s = 0

if 12 <= tempo <= 15:
    tempo12s15s += 1

for nadador in range (2,8):
    nome = input('Nadador 1: ')
    tempo = float(input('Tempo do nadador 1: '))

    if tempo < melhortempo:
        melhornadador = nome
        melhortempo = tempo

    elif tempo > piortempo:
        piornadador = nome
        piortempo = tempo

    somatempo += tempo

    if 12 <= tempo <= 15:
        tempo12s15s += 1

print(f'{melhornadador} é o melhor nadador com {melhortempo} seg.\n{piornadador} é o pior nadador com {piortempo} seg.')

media = somatempo / 7

print(f'Média de tempos = {media:.2f} seg.\nAtletas entre 12s e 15s: {tempo12s15s}')








    



