valor1 = int(input('Entre com um valor:'))
valor2=int(input('Entre com outro valor:'))

if valor1>valor2:
  print('\033[4;31mO Primeiro Valor é o maior!')
elif valor2>valor1:
    print('\033[4;31mO Segundo Valor é o maior!')
elif valor1==valor2:
  print('\033[4;33mNão existe valor maior, os dois são iguais!')

