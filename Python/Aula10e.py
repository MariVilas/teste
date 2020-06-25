a=int(input('Entre com um ano:'))
print('Vamos calcular se ele é bissexto....')
if a%4 == 0:
  if a%100 == 0:
    if a%400 == 0:
      print('Esse ano é bissexto!')
else:
    print('Esse não é um ano Bissexto!')
