

valorCasa = float(input('Qual o valor da casa R$ '))
salarioComprador = float(input('Qual o salário do comprador R$ '))
qntAnos = float(input('Em quantos anos ele irá pagar: '))

meses = qntAnos * 12

prestacao = valorCasa / meses

if prestacao > salarioComprador * 0.3:
    print('Empréstimo negado! ')
else:
    print('Empréstimo aceito!')
    

