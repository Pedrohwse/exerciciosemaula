'''lista = ['Pedro', 'José', 'Maria', 'Carlos']

listaa = ['Mateus']''''''
''
#for n in range(0, len(lista)):
    print(lista[n], end= ' ')

lista.append('Jorge')   #adc nome

lista.insert(0,'Jorge')'''      #adc nome em lugar especifico

'''lista.sort()''' #ordem crescente'''

'''lista.sort(reverse = True) #decrescente'''

'''del lista [3]'''

'''lista.remove('Pedro')'''

'''lista.pop() #ultimo elemento apagar'''

'''lista.clear() #limpar lista\vazia'''

'''listaa = lista'''

'''listaa = lista[:] #fatiar sem atribuir o mesmo'''

'''lista.append('José')'''

'''lista.extend(listaa) #unir duas listas'''

'''print(lista.count('Mateus')) #quantas vezes a palavra aparece'''

'''print(lista.index('Pedro')) #ver a posição da palavra'''

'''for indice,nome in enumerate(lista):       
    print(f'{nome} está armazenado no índice {indice}')'''
    #'''#indice + print o valor da posição e o indice'''


a = [ [2,1,-5] , [3,7,0] , [6,4,8]]

'''print(a[0][0])''' #linha zero e a coluna zero
'''print(a[0][0] +a [0][1] +a [0][2])''' #somar

soma_a = 0
lin = len(a)
col = len(a[0])


for i in range(lin):  #soma
    for j in range(col):
        soma_a += a[i][j]

print(soma_a)


