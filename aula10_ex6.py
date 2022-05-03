from random import choice


itens = (0,1,2)


print ('Escolha dentre as opções: \n 0. Pedra \n 1. Papel \n 2. Tesoura')

jogador = int(input('Qual é a sua jogada?'))

computador = choice (itens)

if jogador == computador:
    print('Empate, eu escolhi'.format(jogador))

elif jogador == 0 and computador == 1:
    print('Você ganhou! Eu escolhi Papel!'.format(computador))

elif jogador == 0 and computador == 2:
    print('Você ganhou! Eu escolhi Tesoura!'.format(computador))

elif jogador == 1 and computador == 0:
    print('Você Perdeu! Eu escolhi Pedra!'.format(computador))

elif jogador == 1 and computador == 2:
    print('Você perdeu! Eu escolhi Tesoura!'.format(computador))

elif jogador == 2 and computador == 0:
    print('Você Perdeu! Eu escolhi Pedra!'.format(computador))

elif jogador == 2 and computador == 1:
    print('Você ganhou! Eu escolhi Papel!'.format(computador))









