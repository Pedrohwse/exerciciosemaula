valorCamiseta = float(input('Digite um valor: R$'))
quantidade = float(input('Quantas camisetas você irá comprar? '))

if quantidade <=5:
    desconto = valorCamiseta - (valorCamiseta * 0.03)
    print('O valor é de R${:.2f}, e com desconto passa a ser R${:.2f}'.format(valorCamiseta,desconto))

elif quantidade > 5 and quantidade <= 10:
    desconto = valorCamiseta - (valorCamiseta * 0.05)
    print('O valor é de R${:.2f}, e com desconto passa a ser R${:.2f}'.format(valorCamiseta,desconto))

elif quantidade >=10:
    desconto = valorCamiseta - (valorCamiseta * 0.07)
    print('O valor é de R${:.2f}, e com desconto passa a ser R${:.2f}'.format(valorCamiseta,desconto))




