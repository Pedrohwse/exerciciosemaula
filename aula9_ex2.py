num = int(input('Digite um número: '))

esc = int(input('Digite 1 para Binário, 2 para Octal ou 3 para hexadecimal'))


if esc == 1:
    print('O número {} em binário fica {}.'.format(num,bin(num)))

elif esc == 2:
    print('O número {}, em octal fica {}.'.format(num,oct(num)))

elif esc == 3:
    print('O número {}, em hexadecimal fica {}.'.format(num,hex(num)))