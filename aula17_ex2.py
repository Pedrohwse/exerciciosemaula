'''Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,
desconsiderando os espaços'''

'''frase = input('Digite uma frase: ').strip().upper()

palavras = frase.split()
junto = ''.join(palavras)
inverso = ''

for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]

if inverso == junto:
    print('Temos um palíndromo!')

else:
    print('A frase digitida não é um palíndromo!')'''

frase = input('Digite uma frase: ').strip().upper()

palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
print(f'O inverso de {junto} é {inverso}')


if inverso == junto:
    print('Temos um palíndromo!')

else:
    print('A frase digitida não é um palíndromo!')
