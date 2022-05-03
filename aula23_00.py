# converter tupla em lista

'''dias =('domingo', 'segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sábado')

semana = list(dias)

print(f'A variavel semana é do tipo {type(semana)} e contém os dias da semana {dias}')'''

num = []
for n in range(0,10):
    num.append(n**2)

print(num)

lista1 = [x**2 for x in range(10)] #numeros elevados ao quadrado entre 0 e 10
print(lista1)

lista2 = [x for x in range(1,20) if x%2==0] #numeros pares entre 1 e 20
print(lista2)

lista3 = [i for i in "HACKATHON" if i in ['A', 'E', 'I', 'O', 'U']] #inserindo vogais
print(lista3)

lista4 = [1,2,3]
lista4 = [i**3 for i in lista4] #atribuir novos valores aos elementos atraves de uma operacao
print(lista4)
