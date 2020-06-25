import os

produto = float(input("Digite o preço do produto: "))
pagamento =int(input("Digite a forma de pagamento: "))
vista=1
v= produto-(produto*10//100)
cartao=2
c= produto-(produto*5//100)
n=produto
prazo=4
p= produto+(produto*20/100)
if pagamento == 1:
    print("Dinheiro ou Cheque 10% de Desconto",v)
elif pagamento== 2:
    print("À Vista no Cartão 5% de Desconto",c)
elif pagamento==3:
    print("Em 2X, Preço Normal",n)
elif pagamento ==4:
    print("20% de Acréscimo",p)
