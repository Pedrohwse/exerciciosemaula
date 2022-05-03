from random import randint

computador = randint (0,5)

print('Vou pensar em um número entre 0 e 5, tente advinhar.')

jogador = int(input('Em que número estou pensando ?'))

if jogador == computador:
    print(' Você acertou!')
else:
    print('Você errou, eu escolhi o número {}!'.format(computador))
    
