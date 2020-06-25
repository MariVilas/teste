valor1 = int(input('Entre com sua idade:'))
conta= 18 - valor1
if valor1<18:
  print('\033[4;31mVocê ainda não deve se alistar!','Falta',conta,' Anos para o seu alistamento!')
elif valor1==18:
    print('\033[4;31mEstá na hora de se alistar!')
elif valor1>18:
  print('\033[4;33mSeu tempo para se alistar já passou!')