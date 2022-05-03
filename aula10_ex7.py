
print('-'*25)
print('Solicite o cargo abaixo: \n 1.Programador de Sistemas \n 2.Analista de Sistemas \n 3.Analista de Banco de Dados')
print('-'*25)

cargo = float(input('Digite seu cargo: '))
salario = float(input('Qual o seu salário? R$'))

if cargo == 1:
    aumento = salario + (salario*0.3)
    print('Seu salário com o aumento será de: R${:.2f}'.format(aumento))

elif cargo == 2:
    aumento = salario + (salario*0.2)
    print('Seu salário com o aumento será de: R${:.2f}'.format(aumento))

elif cargo == 3:
    aumento = salario + (salario*0.15)
    print('Seu salário com o aumento será de: R${:.2f}'.format(aumento))
    


    



