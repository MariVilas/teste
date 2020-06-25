import math
resp = 'SN'

print("-=" * 20)
print("Seja bem-vindo a quitanda do Gesonel!")
print("-=" * 20)
quantidade = (float(input('Entre com a quantidade:')))
perguntar = int(input('''Escolha uma opcao para comprar: 


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



if perguntar == 0:
 print('O valor da sua compra de banana é de R$',quantidade * 1.99// 1000)
if perguntar == 1:
 print('O valor da sua compra de maçã é de R$',quantidade * 3.99 // 1000)
if perguntar == 2:
 print('O valor da sua compra de pera é de R$',quantidade * 8.90 // 1000)
if perguntar == 3:
 print('O valor da sua compra  de laranja é de R$',quantidade * 1.39//1000)
if perguntar == 4:
 print('O valor da sua compra de batata é de R$',quantidade * 3.49// 1000)
if perguntar == 5:
 print('O valor da sua compra de cenoura é de R$',quantidade * 2.59 // 1000)
if perguntar == 6:
 print('O valor da sua compra de vagem é de R$',quantidade * 9.90 // 1000)
if perguntar == 7:
 print('O valor da sua compra de mandioca é de R$',quantidade * 0.99//1000)
if perguntar == 8:
 print('O valor da sua compra de pepino é de R$',quantidade *2.59 //1000)
else:
 resp = str(input('Quer continuar?[S/N]')).upper().strip()[0]
 if resp == 'N':
   print("-=" * 20)
 print("-=" * 20)
 print("-=" * 20)
 print('Obrigada por utilizar nossos serviços!!!')
 print("-=" * 20)
 print("-=" * 20)
 print("-=" * 20)

