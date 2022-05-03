

print('1. À vista dinheiro/cheque')
print('2. À vista no cartão')
print('3. Em até 2x no cartão')

op = float(input('Diga sua forma de pagamento: '))

if op == 1:
    valor = float(input('Qual o valor do produto? R$'))
    desconto = valor - (valor*0.1)
    print('O valor é de R${:.2f}, e com desconto passa a ser R${:.2f}'.format(valor,desconto))

elif op == 2:
    valor = float(input('Qual o valor do produto? R$'))
    desconto = valor - (valor*0.05)
    print('O valor é de R${:.2f}, e com desconto passa a ser R${:.2f}'.format(valor,desconto))

elif op == 3:
    valor = float(input('Qual o valor do produto? R$'))
    print('O valor é de R${:.2f}'.format(valor))
    





