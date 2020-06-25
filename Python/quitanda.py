import math
from time import sleep
resp = 'SN'
while True:
    print("-=" * 20)
    print("Seja bem-vindo a quitanda do Gesonel!")
    print("-=" * 20)
    quantidade=(float(input('Entre com a quantidade:')))
    preço=(float(input('Entre com o preço:')))
    perguntar = int(input('''Escolha uma opcao de produto:: 
        
    
    [0] Banana
    [1] Maçã
    [2] Pera
    [3] Laranja
    [4] Batata
    [5] Cenoura
    [6] Vagem
    [7] Mandioca
    [8] Pepino
    
    
    Digite sua escolha: '''))
    total = (quantidade * preço) / 1000
    total = round(total, 2)


    print("CAL\n")
    sleep(1)
    print("CU\n")
    sleep(1)
    print("LANDO!!!\n")
    print("-=" * 20)
    print("-=" * 20)


    if perguntar == 0:
      print('O valor da sua compra de banana é de R$',total)
    if perguntar == 1:
      print('O valor da sua compra de maçã é de R$',total)
    if perguntar == 2:
      print('O valor da sua compra de pera é de R$',total)
    if perguntar == 3:
     print('O valor da sua compra  de laranja é de R$',total)
    if perguntar == 4:
     print('O valor da sua compra de batata é de R$',total)
    if perguntar == 5:
     print('O valor da sua compra de cenoura é de R$',total)
    if perguntar == 6:
     print('O valor da sua compra de vagem é de R$',total)
    if perguntar == 7:
     print('O valor da sua compra de mandioca é de R$',total)
    if perguntar == 8:
     print('O valor da sua compra de pepino é de R$',total)

    resp = str(input('Quer continuar?[S/N]')).upper().strip()[0]
    if resp == 'N':
        break
print("-=" * 20)
print("-=" * 20)
print("-=" * 20)
print('Obrigada por utilizar nossos serviços!!!')
print("-=" * 20)
print("-=" * 20)
print("-=" * 20)
