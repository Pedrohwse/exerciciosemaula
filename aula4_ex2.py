from math import sqrt

x1=float(input('Qual o valor de x1?'))
y1=float(input('Qual o valor de y1?'))

x2=float(input('Qual o valor de x2?'))
y2=float(input('Qual o valor de y2?'))

d=sqrt(x2-x1)**2+(y2-y1)**2

print('A distancia entre P1 e P2 é {:.2f}'.format(d))

