
from time import sleep

lista = ("À Vista", "Cartão à Vista", "Preço Fechado","À Prazo")
produto1=int(input('Entre com o valor do produto:'))
produto2=int(input('Entre com o valor do produto:'))
produto3=int(input('Entre com o valor do produto:'))
produto4=int(input('Entre com o valor do produto:'))
produto5=int(input('Entre com o valor do produto:'))
produto6=int(input('Entre com o valor do produto:'))
perguntar = int(input('''Escolha uma opção para sua compra: 

[0] À Vista
[1] Cartão à Vista
[2] Preço Fechado
{3} À Prazo

Digite sua escolha: '''))

print("CAL\n")
sleep(1)
print("CU\n")
sleep(1)
print("LANDO!!!\n")

lista1= produto1+produto2+produto3+produto4+produto5+produto6
v= lista1 -(lista1*10/100)
c= lista1 -(lista1*5/100)
p= lista1
pz= lista1 +(lista1*20/100)


if perguntar == 0:
     print("Você tem 10% de desconto! O valor da sua compra é de:",v)
elif perguntar ==1:
     print("Você tem 5% de desconto! O valor da sua compra é de:",c)
elif perguntar == 2:
    print("Você paga o preço fechado! O valor da sua compra é de:",p)
else:
    print("Você tem 20% de Acréscimo! O valor da sua compra é de:",pz)


