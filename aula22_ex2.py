'''Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Brasileirão na ordem de 
colocação. Depois mostre:a) os cinco primeiros b) os últimos 4 colocados c) times em ordem alfabética 
e d) em que posição está o time Chapecoense'''


times = ('Bahia', 'Chapecoense', 'Sport', 'Grêmio', 'Cruzeiro',
 'Brusque', 'Naútico', 'Vasco', 'Ituano', 'Londrina', 'Sampaio',
  'Criciuma', 'Operario', 'Guarani', 'Ponte',
   'Tombense', 'VN', 'CSA', 'Novo', 'CRB')


print(f'Cinco primeiros colocados: {times[0:5]}')

print(f'Quatro ultimos colocados: {times[-4:]}')

clubes = times.index('Chapecoense')
print(f'A Chapecoense está na {clubes + 1} º posição ')



