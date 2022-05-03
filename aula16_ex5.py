'''Crie um programa no qual o usuário informe a idade de um número indeterminado de alunos. Para
encerrar a leitura dos dados, o usuário deve informar uma idade negativa. No final, o programa deve
mostrar a média aritmética entre a maior e a menor idade.'''

maior = 0
menor = 0

idade = int(input('Idade: '))

maisnovo = idade
maisvelho = idade

while True:
    idade = int(input('Idade: '))
    if idade < 0:
        break

    if idade < maisnovo:
        maisnovo = idade

    elif idade > maisvelho:
        maisvelho = idade

media = (maisnovo + maisvelho) / 2

print(f'Menor idade: {maisnovo} \nMaior idade: {maisvelho} \nMédia entre as idades: {media:.2f}')



    