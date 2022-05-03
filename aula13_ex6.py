#Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre
#os 10 primeiros termos dessa progressão.

a1 = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))

decimo_termo = a1 + (9 * r)

for c in range (a1, decimo_termo + r, r):
    print('{}'.format(c), end='-')
print('Fim')



