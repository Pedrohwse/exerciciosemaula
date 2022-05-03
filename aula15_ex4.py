'''Para construir o programa a seguir, considere que os usuários só informarão números inteiros positivos.
Crie um programa que receba 5 números digitados e, ao fim, exibir quantos números são pares.'''
pares = 0
for p in range(5):
    num = int(input('Digite um número: '))

    if num %2 == 0:
        pares +=1
print('Dos 5 números inteiros, {} são pares!'.format(pares))
