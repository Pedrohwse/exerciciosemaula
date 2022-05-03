#Faça um programa que leia um número inteiro qualquer e mostre na tela sua tabuada.

num = int(input('Digite um número: '))  
for c in range(1,11):
  print('{} X {} = {}'.format(num, c, num * c))
  
  