

print('Grandezas Elétricas')
print('1. Tensão (em Volt)')
print('2. Resistência (em Ohm)')
print('3. Corrente (em Ampére)')

op = int(input('Qual a grandeza deseja calcular? '))

if op < 1 or op > 3:
    print('Opção Inválida.')
elif op == 1:
    R = float(input('Digite o valor da corrente em Ohm: '))
    I  =float(input('Digite o valor da corrente em Ampére: '))
    U = R * I
    print('R = {:.2f}'.format(U))
elif op == 2:
    U = float(input('Digite o valor da tensão em Volts: '))
    I = float(input('Digite o valor da corrente em Ampére: '))
    R = U / I
    print('R = {:.2f}'.format(R))
else:
    U = float(input('Digite o valor da tensão em Volts: '))
    R = float(input('Digite o valor da corrente em Ohm: '))
    I = U / R
    print('I = {:.2f}'.format(I))
    

