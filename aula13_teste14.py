

while True:
    n1 = int(input('Digite o primeiro número: '))
    n2 = int(input('Digite o segundo número: '))

    if n2 == 0:
        print('Divisor não pode ser 0. \n Programa será encerrado...')
        break
    divisao = n1 / n2
    print('{} / {} = {:.2f}'.format(n1,n2,divisao))
    
