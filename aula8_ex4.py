from random import choice

a1 = input('Digite um nome: ')
a2 = input('Digite um nome: ')
a3 = input('Digite um nome: ')
a4 = input('Digite um nome: ')

nome = (a1,a2,a3,a4)
sorteio = choice(nome)

print('O escolhido pelo professor para apagar o quadro será {}'.format(sorteio))





