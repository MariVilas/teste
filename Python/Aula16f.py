listagem= ('Macarrão',1.95,
           'Açúcar',1.79,
           'Pó de Café',5.69,
           'Arroz',10.98,
           'Feijão',4.98,
           'Leite',2.39,
           'Farinha de Trigo',2.39,
           'Molho de Tomate',0.99,
           'Margarina',2.98)

print('-'*40)
print(f'{"Cupom Fiscal":^40}')
print(f'{"Atacadão/SA":^40}')
print('-'*40)
for pos in range(0,len(listagem)):
    if pos %2==0:
        print(f'{listagem[pos]:.<30}',end='')
    else:
        print(f'R${listagem[pos]:.>7.2f}')