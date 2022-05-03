print('## Programa de emprestimos ## \n Responda: 0 - Não e 1 - Sim')
nomeNegativado = int(input ('Possuí nome negativado?'))

if nomeNegativado == 1:
    print('Não pode realizar o emprestimo.')
else:
    carteiraAssinada = int(input(' Possui carteira assinada? '))
    if carteiraAssinada == 0:
        print('Não pode realizar o emprestimo')
    else:
        possuiCasapropria = int(input('Possui casa própria? '))
        if possuiCasapropria == 0:
            print('Não pode realizar o empréstimo.')
        else:
            print('Concede o empréstimo')



