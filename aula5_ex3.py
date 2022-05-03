
from math import radians
from math import sin
from math import cos
from math import tan

a=float(input('Digite o valor de um angulo:'))

s=sin(radians(a))
c=cos(radians(a))
t=tan(radians(a))

print('O angulo {:.2f} tem como:. \n seno{:.2f}. \n cosseno{:.2f}. \n tangente{:.2f}'.format(a,s,c,t))


