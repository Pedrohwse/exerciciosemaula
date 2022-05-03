#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso
#esteja errado, peça a digitação novamente até ter um valor correto.

sexo = str(input('Qual seu sexo? [M/F]: ')).strip().upper()

while sexo != 'M' and sexo != 'F':

    print('Você não digitou M ou F')

    sexo = str(input('Qual seu sexo? [M/F]: ')).strip().upper()
print('Correto!')
    
    