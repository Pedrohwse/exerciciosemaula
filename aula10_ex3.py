

peso = float(input('Digite seu peso: ' ))
altura = float(input('Digite sua altura: '))

imc = peso / (altura**2)
massaCorporal = imc
if imc < 18.6:
    print('Sua massa corporal é de {:.2f}, você está ABAIXO do peso!'.format(massaCorporal))

elif imc >= 18.5 and imc <= 25:
    print('Sua massa corporal é de {:.2f}, você está com o PESO IDEAL!'.format(massaCorporal))

elif imc > 25 and imc <= 30:
    print('Sua massa corporal é de {:.2f}, você está SOBREPRESO!'.format(massaCorporal))

elif imc > 30 and imc <= 40:
    print('Sua massa corporal é de {:.2f}, você está OBESO!'.format(massaCorporal))

elif imc > 40:
    print('Sua massa corporal é de {:.2f}, você se encontra em OBESIDADE MÓRBIDA'.format(massaCorporal))
    
    