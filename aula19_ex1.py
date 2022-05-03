'''Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros
elementos de uma Sequência de Fibonacci. Ex.: 0 -> 1 ->1 -> 2-> 3 -> 5-> 8.'''

n = int(input('Digite um número inteiro: '))    
n1 = 0
n2 = 1
print(f'{n1} -> {n2}', end= ' ')

for c in range(n-1):
    n3 = n1 + n2
    print(f'-> {n3}', end=' ')
    n1 = n2
    n2 = n3











