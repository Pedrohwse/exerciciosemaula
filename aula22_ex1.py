''' Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, 
mostre: a) quantas vezes apareceu o valor 9 b) em que posição foi digitado o primeiro valor 3 e c) quais 
foram os números pares.'''

#Usando Tupla
 
num = int(input('Digite um valor ')), int(input('Digite um valor ')), int(input('Digite um valor ')), int(input('Digite um valor '))


if 9 in num:
     print(f'O valor apareceu {num.count(9)} vezes')

else:
         print('O número 9 não foi informado')

if 3 in num:
    print(f'O número 3 foi digitado na {num.index(3)+1} ª posição')
else:
    print('O número 3 não foi informado')

    for n in num:
        if n%2 == 0:
            print(n, end= ' ')



    





