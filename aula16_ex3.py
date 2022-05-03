'''Imagine um sistema de caixa eletrônico. Construa um programa que receba a senha de um correntista para
validar o seu acesso ao sistema. Considere que a senha fictícia do correntista é 123456. Considere as seguintes
restrições: a) quando a senha estiver correta, mostrar a mensagem: “Olá, <SEUNOME>. Seja bem-vindo ao nosso
banco!" b) quando o usuário errar a senha pela primeira vez, mostrar a mensagem: “Senha incorreta! Você ainda
tem 2 tentativas.” c) se o usuário errar a senha pela segunda vez, mostrar a mensagem: “Senha incorreta! Você
ainda tem 1 tentativa.” d) se o usuário errar a senha novamente, mostrar a mensagem “Sua senha foi bloqueada!
Por favor, dirija-se a um de nossos caixas.” e o programa deve ser encerrado.'''

for c in range(3,0,-1):
    nome = input('Digite seu nome: ')
    senha = int(input('Digite sua senha: '))
    if senha == 123456:
        print('Olá, {}. Seja Bem vindo ao nosso banco!'.format(nome))
        break

    elif senha != 123456:
        print('Senha incorreta! Você ainda tem {} tentavia(s).'.format(c-1))
        
        if c == 1:
            print('Sua senha foi bloqueada! Por favor, dirija-se a um dos nossos caixas.')
            break





