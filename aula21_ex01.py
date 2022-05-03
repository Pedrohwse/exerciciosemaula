lista = [12, -2, 4, 8, 29, 45, 78, 36, -17, 2, 12, 8, 3, 3, -52]

maiorvalor = lista[0]
menorvalor = lista[0]
listaPares = []
ocorrencia = 0
mediaElementos = 0
somaNegativa = 0

for index in range(0,len(lista)):
    if maiorvalor < lista[index]: #MAIOR VALOR
        maiorvalor = lista[index]

    if menorvalor > lista[index]: #MENOR VALOR
        menorvalor = lista[index]

    if lista[index] %2 == 0: #PARES
        listaPares.append(lista[index])

    if lista[index] == lista[0]: #QUANTAS VEZES O PRIMEIRO NUMERO
        ocorrencia += 1

    mediaElementos += lista[index] #MEDIA


    if lista[index] < 0:
        somaNegativa += lista[index] #NEGATIVOS

mediaElementos /= len(lista)

print(f'Maior valor: {maiorvalor}')
print(f'Menor valor: {menorvalor}')
print(f'Lista de números pares: {listaPares}')
print(f'Número de ocorrencia do primeiro elemento: {ocorrencia}')
print(f'Média de elementos: {mediaElementos:.2f}')
print(f'Elemenos negativos: {somaNegativa}')






