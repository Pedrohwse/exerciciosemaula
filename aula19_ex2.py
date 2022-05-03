'''Crie um programa que leia vários números inteiros pelo teclado. O programa só vai para quando o
usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram
digitados e qual foi a soma entre eles (desconsiderando o flag).'''

num = soma = quantidade = 0

num = int(input('Digite um numero ou 999 para parar: '))

while num != 999:
    soma += num
    quantidade += 1
    num = int(input('Digite um numero ou 999 para parar: '))

print(f'Foram digitados ao todo {quantidade} numeros e a soma dos valores é {soma}')








