valor1 = int(input('Entre com sua primeira nota:'))
valor2= int(input('Entre com sua segunda nota:'))
media= (valor1+valor2)//2
if media<5:
  print('\033[4;31mReprovado')
elif media ==5 and media<=6.9 :
    print('\033[4;31mRecuperação!')
elif valor1>=7:
  print('\033[4;33mAprovado!')