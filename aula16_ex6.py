'''Crie um programa no qual o usuário informe o código do cargo de um funcionário (ver tabela
abaixo) e o seu respectivo salário. Para encerrar a leitura dos dados, defina uma condição de parada (por
exemplo, código do cargo igual a zero). Ao fim, o programa deve informar a média salarial dos
nutricionistas.'''

print('Código de cargo: \n1 : Enfermeiro \n2 : Nutricionista \n3 : Médico(a)')

qtdenutri = 0 
total_sal_nutri = 0

while True:
    cargo = int(input('Informe um códico de cargo: '))
    if cargo >= 1 and cargo <= 3:
        salario = float(input('Salário R$: '))
        if cargo == 2:
            qtdenutri += 1
            total_sal_nutri + salario

        resp = input('Dseja continuar [S/N]: ')
        if resp.upper() == 'N':
            break
    else:
        print('Código inválido!')

if qtdenutri > 0:
    media = total_sal_nutri / qtdenutri
    print(f'Média salarial dos nutricionistas R$: {media:.2f}')

else:
    print('Não foram inseridos dados sobre os nutricionistas')
    