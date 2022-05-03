'''dias = ('domingo', 'segunda' , 'terça', 'quarta', 'quinta' , 'sexta', 'sabádo') #tupla

print(type(dias))

print(dias[3])'''

'''texto = 'python'
print(tuple(texto)) #divisão em letras'''

'''lista = [1, 2, 3, 4] #'' em números
lista[2] = 8
print(tuple(lista))'''

'''lista = [3, 5]       #nao vou mexer TUPLA   preciso mexer LISTA
tupla1 = (1, 2, lista)
tupla2 = (1, 2, lista[0], lista[1])  #variavel com 4 indices

#print(tupla)
#print(tupla[2])

#print(len(tupla2))

print(tupla2.count(2))'''

'''lista = ['python', 1, 2, 'java']
print(lista)'''

meses = ['janeiro','fevereiro','março','abril','maio','junho','julho','agosto','setembro','outubro','novembro', 'dezembro']

'''n = 1

while n < 4:
    mes = int(input('Escolha um mês [1-12]:'))
    if 1 <= mes < 13:
        print(f'O mês é {meses[mes - 1]}')
    n += 1'''

'''print(meses[-3:])'''

#meses.append('janaina') #apenas para lista, adicionar ou adicionar dois por vez meses+=['janaina','zé]
#print(meses*2)

for mes in meses: #um abaixo do outro
    print(mes, end=' ') # um ao lado do outro











