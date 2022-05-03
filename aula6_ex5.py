

num = int(input('Digite um número: '))
if num%2 == 0:
    quadrado= num**2
    print('{} é par e seu quadrado é {}'.format(num,quadrado))
else:
    cubo = num**3
    print('{} é impar e seu cubo é {}'.format(num,cubo))
    