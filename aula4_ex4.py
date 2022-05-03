n=input('Qual o nome do corretor?')
q=float(input('Qual a quantidade de imoveis?'))
v=float(input('Qual valor total de vendas?'))

f= 1500+(200*q)+(0.05*v)

print('O salario final do corretor será{:.2f}'.format(f))


