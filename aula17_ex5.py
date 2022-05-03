'''Crie um programa que leia o nome e o preço de vários produtos. O programa deverá
perguntar se o usuário vai continuar. No final, mostre: a) qual é o total gasto na compra b)
quantos produtos custam mais de R$1000 c) qual é o nome do produto mais barato.'''

total = totmil = menor = cont = 0
barato = ' '
while True:
    produto = input('Nome do produto: ')
    preco = float(input('Preço: R$: '))
    cont += 1
    total += preco

    if preco > 1000:
        totmil += 1

    if cont == 1 or preco < menor:
        menor = preco
        barato = produto
    resp = ' '

    while resp not in 'SN':
        resp = input('Quer continuar [S/N]?').strip().upper()

    if resp == 'N':
        break
print(f'O total das compras foi R${total:.2f}')
print(f'Temos {totmil} produtos custando mais de R$1000,00.')
print(f'O produto mais barato é o {produto} que custa R${menor:.2f}')



