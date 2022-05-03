
'''Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a
média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao
usuário se ele quer ou não continuar a digitar valores.'''

resp = 'S'
soma = quantidade = media = maior = menor = 0

while resp in 'S':
    num = int(input('Digite um número: '))
    soma += num
    quantidade += 1

    if quantidade == 1:
        maior = menor  = num

    else: 
        if num > maior:
            maior = num

        if num < menor:
            menor = num
    
    resp = input('Quer contiar [S/N]? ').upper().strip()

media = soma / quantidade

print(f'Você digitou {quantidade} números e a média foi {media}')
print(f'O maior valor foi {maior} e o menor valor foi {menor}')



