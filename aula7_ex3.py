
salario=int(input('Qual o salário do funcionario R$: '))


if salario <= 1250:
    novo = salario+(salario*0.15)
else:
    novo = salario+(salario*0.10)

print( 'Quem ganhava R${:.2f} passa a ganhar {:.2f} agora'.format(salario,novo))


    
