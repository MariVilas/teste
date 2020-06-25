d= int(input('Entre com a quantidade de dias alugados:'))
k= int(input('Entre com a quantidade de Km utilizados:'))

p1= d * 60

p2 = k * 0.15

p3 = p1 + p2

print('O valor de diárias é de:',p1,'reais')
print('O valor de kilometragem é de:',p2,'reais')
print('O custo total do aluguel é de:',p3,'reais')