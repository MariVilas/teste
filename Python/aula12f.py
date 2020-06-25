valor1 = int(input('Entre com sua idade:'))

if valor1<=9:
  print('\033[4;31mMirim!')
elif valor1<=14:
  print('\033[4;31mInfantil!')
elif valor1 <= 19:
  print('\033[4;31mJúnior!')
elif valor1<=20:
  print('\033[4;31mSênior!')
elif valor1>20:
  print('\033[4;33mMaster!')