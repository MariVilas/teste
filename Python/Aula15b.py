while True:
  num = int(input('Entre com um número:'))
  if num <= 0 :
      break
  tabuada = num*1,num*2,num*3,num*4,num*5,num*6,num*7,num*8,num*9,num*10
  print(f'A Tabuada do número {num} é {tabuada,}->')
print('Terminado')