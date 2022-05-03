

nota1 = float(input('Informe a nota 1: '))
nota2 = float(input('Informe a nota 2: '))

media= (nota1 + nota2)/2

print('Média: ',media)

if media <= 5:
    print('Reprovado')

elif media >= 5 and media <=7:
    print('Recuperação')

elif media >= 7:
    print('Aprovado')

    