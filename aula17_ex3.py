'''Crie um programa que leia dois valores e mostre um menu como com: 1) somar 2)
multiplicar 3) maior 4) novos números 5) sair do programa. Seu programa deverá realizar a
operação solicitada em cada caso.'''

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))

opcao = 0

while opcao != 5:
    print('''
    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa''')
    opcao = int(input('Qual é a sua opção: '))

    if opcao == 1:
        soma = n1 + n2
        print(f'A Soma entre {n1} e {n2} = {soma}')
    
    elif opcao == 2:
        produto = n1 * n2
        print(f'O produto entre {n1} e {n2} = {produto}')

    elif opcao == 3:
        if n1 > n2:
            maior = n1
        
        else:
            maior = n2
        print(f'entre {n1} e {n2} o maior será {maior}')

    elif opcao == 4:
        print('Informe novos números ')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))

    elif opcao == 5:
        print('Finalizando...')

    else:
        print('Opção Inválida')
    print('#' *10)

print('Fim')

    
