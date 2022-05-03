
km = float(input('Quantos kms foram percorridos: '))
dia = int(input('Por quantos dias ele foi alugado: '))

preco = dia*60
km_rodado = km*0.15
valor_total = preco+km_rodado
 
print('O carro foi alugado por {} dias pelo  preço de R${}. Foram percorridos {}Km, seu preço final será R${}'.format(dia,preco,km,valor_total))




