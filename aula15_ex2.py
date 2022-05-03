'''Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.'''

maior = 0
menor = 500

for c in range(0,5):
    peso = float(input('Informe seu peso: '))
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso
print('O maior peso foi {:.2f} e o menor peso foi {:.2f}'.format(maior,menor))



