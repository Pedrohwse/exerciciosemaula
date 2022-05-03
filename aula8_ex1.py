preco = float(input('Digite o preço de um produto:R$'))

novo_preco = preco - (preco*0.05)
print('o preço atual do produto é R${}, e com o desconto fica R${}'.format(preco,novo_preco))