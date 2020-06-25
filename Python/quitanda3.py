import math
resp = 'SN'

print("-=" * 20)
print("Seja bem-vindo a quitanda do Gesonel!")
print("-=" * 20)
quantidade = (float(input('Entre com a quantidade:')))
perguntar = (float(input('Entre o valor do produto por KG:')))
quantidade1 = (float(input('Entre com a quantidade:')))
perguntar1 = (float(input('Entre o valor do produto por KG:')))
quantidade2 = (float(input('Entre com a quantidade:')))
perguntar2 = (float(input('Entre o valor do produto por KG:')))
quantidade3 = (float(input('Entre com a quantidade:')))
perguntar3 = (float(input('Entre o valor do produto por KG:')))

preço= quantidade*perguntar//1000
preço1= quantidade1*perguntar1//1000
preço2= quantidade2*perguntar2//1000
preço3= quantidade3*perguntar3//1000

soma= preço+preço1+preço2+preço3
print('O valor total da compra é de R$',soma)



print("-=" * 20)
print("-=" * 20)
print("-=" * 20)
print('Obrigada por utilizar nossos serviços!!!')
print("-=" * 20)
print("-=" * 20)
print("-=" * 20)

