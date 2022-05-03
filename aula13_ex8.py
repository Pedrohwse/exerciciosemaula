#Crie um programa no qual o usuário informe um número inteiro positivo N e armazene-o
#em uma variável. Em seguida, o usuário deve digitar N números. Ao fim, o programa deve
#imprimir a média aritmética dos N números digitados.

n = int(input('Digite a quantiade de números a informar: '))

soma = 0

for cont in range(n):
    num = float(input('Digite um número: '))
    soma += num
media = soma / n
print('Média: {:.2f}'.format(media))

