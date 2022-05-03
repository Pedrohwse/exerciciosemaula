

from random import shuffle

a1 = input('Primeiro aluno: ')
a2 = input('Segundo aluno: ')
a3 = input('Terceiro aluno: ')
a4 = input('Quarto aluno: ')

aluno = [a1,a2,a3,a4]

print('Os alunos que compõe a turma são {}'.format(aluno))

shuffle(aluno)

print('A ordem de apresentação será {}'.format(aluno))


