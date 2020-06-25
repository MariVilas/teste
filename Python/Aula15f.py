resp='S N'
soma=menor=caro=cont=0
while True:
    print("-=" * 20)
    print("-=" * 20)
    print("-=" * 20)
    print('**Loja do Zubiano**')
    preço=float(input('Entre com o preço do produto R$'))
    nome=str(input('Entre com o nome do produto:'))
    cont+=1
    soma += preço
    if preço > 1000:
     caro+=1
    if cont == 1:
      menor = preço
    else:
     if preço < menor:
          menor = preço

     resp = str(input('Quer continuar?[S/N]')).upper().strip()[0]
     if resp == 'N':
        break
print("-=" * 20)
print('O total de gastos é de:R$',soma)
print('O número de produtos que custam mais de R$1.000 é de:',caro)
print('O  produto mais barato custa R$',menor)
print("-=" * 20)
print("-=" * 20)
print("-=" * 20)