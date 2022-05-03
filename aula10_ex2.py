

r1 = float(input('Digite o valor da primeira reta: '))
r2 = float(input('Digite o valor da segunda reta: '))
r3 = float(input('Digite o valor da terceira reta: '))

if r1 + r2 < r3 and r2 + r1 < r2 and r3 + r1 < r2:
    print ('Estas retas não formam um triângulo')


elif (r1==r2) and (r1==r3):
    print('É UM TRIÂNGULO EQUILÁTERO')

elif ((r1==r2) or (r1==r3)) or (r2==r3):
    print('É UM TRIâNGULO ISÓSCELES')

else:
    print('É UM TRIÂNGULO ESCALENO!')






 



