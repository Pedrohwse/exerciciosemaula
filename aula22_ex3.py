'''Uma turma de formandos está vendendo rifas para angariar recursos financeiros para sua 
cerimônia de formatura. Construa um programa para cadastrar os nomes das pessoas que compraram a 
rifa. Ao fim, o programa deve sortear o ganhador do prêmio e imprimir o seu nome.'''
from random import shuffle, choice

rifa = [] 
while True:
    nomes = input('Comprador: ')
    rifa.append(nomes)
    resp = input('Deseja continuar? S/N ')

    if resp.upper() == 'N':
        break

shuffle(rifa)
sorteado = choice(rifa)

print(f'O comprador sorteado foi: {sorteado}')








