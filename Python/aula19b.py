from time import sleep
from random import randint
resp = 'SN'
dado={}
while True:
    dado['nome1'] = str(input('Nome: '))
    dado['jogada1']= randint(1,6)
    dado['nome2'] = str(input('Nome: '))
    dado['jogada2'] = randint(1, 6)
    dado['nome3'] = str(input('Nome: '))
    dado['jogada3'] = randint(1, 6)
    dado['nome4'] = str(input('Nome: '))
    dado['jogada4'] = randint(1, 6)

    print("JO\n")
    sleep(1)
    print("GAN\n")
    sleep(1)
    print("DO!!!\n")

    print("-=" * 20)
    print("-=" * 20)

    print(dado)

    resp = str(input('Quer continuar?[S/N]')).upper().strip()[0]
    if resp == 'N':
       break
print("-=" * 20)
print('Finalizando!!!')
print("-=" * 20)