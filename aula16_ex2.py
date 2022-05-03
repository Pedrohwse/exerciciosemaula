''' Construa um programa que receba o nome e o preço de 5 medicamentos de uma drogaria (considere que o
usuário informou cinco medicamentos distintos). O programa deve informar o nome e o preço do medicamento
mais barato, bem como a média aritmética dos preços informados.'''
soma = 0

medicamento = input('Informe o medicamento: ')
preco = float(input('Preço: R$'))

maisbarato = medicamento
menorpreco = preco

soma += preco


for c in range(0,4):
    medicamento = input('Informe o medicamento: ')
    preco = float(input('Preço: R$'))
    
    if preco < menorpreco:
        menorpreco = preco
        maisbarato = medicamento
    

    soma += preco

media = soma / 5


print('O medicamento mais barato é o {} que custa R${}, e a média de preços é R${}'.format(maisbarato,menorpreco,media))




    

