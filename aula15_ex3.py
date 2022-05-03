'''Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa mostre: 1) a
média de idade do grupo. 2) qual é o nome do homem mais velho. 3) quantas mulheres têm menos de 20 anos.'''

soma = 0
maioridadehomem = 0
nomemaisvelho = ''
mulhermenor = 0
mediaidade = 0

for p in range(1,5):
    nome = input('Digite seu nome: ').strip()
    idade = int(input('Digite sua idade: '))
    sexo = input('Digite seu sexo: [F/M] ').strip()

    soma += idade
    
    if p == 1 and sexo in 'M':
        maioridadehomem = idade
        nomemaisvelho = nome
    
    if sexo in 'M' and idade > maioridadehomem:
        maioridadehomem = idade
        nomemaisvelho = nome

    if sexo in 'F' and idade < 20:
        mulhermenor += 1

mediaidade = soma /4

print('A média de idade do grupo é de {} anos'.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {}'.format(maioridadehomem,nomemaisvelho))
print('Ao todo serão {} mulher(es) com menos de 20 anos'.format(mulhermenor))





        
