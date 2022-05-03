v = float(input('Digite uma velocidade em km/h?'))

if v > 80:
    print('Você foi multado!')
    multa = (v - 80)*7
    print('Você deve pagar uma multa de R${:.2f}'.format(multa))
else:
    print('Siga livre, dirigindo com cuidado')


