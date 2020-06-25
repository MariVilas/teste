v=int(input('Entre com a velocidade do veículo:'))
if v <=80:
    print('Você é um excelente motorista!')
else:
    d=v-80
    m= d*7
    print('Sua velocidade excedeu o limite em :',d,'km')
    print('E a multa é de:',m,'Reais')


