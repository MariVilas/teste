from time import sleep

n1=int(input('Entre com um número:'))
n2=int(input('Entre com outro número:'))
perguntar =0
while perguntar !=5:
  print('''
  [1] Somar
  [2] Multiplicar
  [3] Subtrair
  [4] Dividir
  [5] Sair do Programa''')

  print("-=" * 20)
  print("-=" * 20)

  perguntar=int(input('Entre com a sua opção:'))

  if perguntar==1:
      print("PEN\n")
      sleep(1)
      print("SAN\n")
      sleep(1)
      print("DO!!!\n")
      print(n1,'+',n2,'=',n1+n2)

  if perguntar==2:
      print("PEN\n")
      sleep(1)
      print("SAN\n")
      sleep(1)
      print("DO!!!\n")
      print(n1,'X',n2,'=',n1*n2)

  if perguntar==3:
      print("PEN\n")
      sleep(1)
      print("SAN\n")
      sleep(1)
      print("DO!!!\n")
      print(n1,'-',n2,'=',n1-n2)

  if perguntar==4:
      print("PEN\n")
      sleep(1)
      print("SAN\n")
      sleep(1)
      print("DO!!!\n")
      print(n1,'%',n2,'=',n1//n2)

else:
      print("PEN\n")
      sleep(1)
      print("SAN\n")
      sleep(1)
      print("DO!!!\n")
      print("Finalizando")



