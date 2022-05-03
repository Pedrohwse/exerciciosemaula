'''Melhore o exercício Ex 1 da Aula 6 onde o computador vai “pensar" em um número entre 0 e 10. Só que
agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para
vencer.'''

from random import randint

computador = randint (0,10)

print('Pense em um número entre 0 a 10!')


acertou = False
palpites = 0

while not acertou:
    jogador = int(input('Qual seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    
    else:
        if jogador < computador:
            print('Mais... tente mais uma vez')
        
        elif jogador > computador:
            print('Menos... tente mais uma vez')
print('Acertou com {} tentativas. Parabéns!'.format(palpites))


