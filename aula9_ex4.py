

idade = float(input('Digite sua idade: '))

falta = 18 - idade
passou = idade - 18

if idade > 18:
    print(' Já passou {} anos do seu alistamento!'.format(passou))

elif idade < 18:
    print('Faltam {} anos para seu alistamento!'.format(falta))
    