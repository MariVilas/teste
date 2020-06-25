resposta='SN'
while True:

    print('-' * 40)
    print(f'{"Transportadora Zubiano":^40}')
    print(f'{"Levando você ao seu destino":^40}')
    print('-' * 40)

    print(f'{"Vamos iniciar a cotação?"}')
    km=(int(input('Entre com a quantidade de KM entre a partida e o destino desejado:')))
    valor= km*10
    itens = (int(input('Entre com a quantidade de itens a serem transportados:')))
    preço = itens * 100
    pet = (int(input('Entre com a quantidade de animais que serão transportados:')))
    custo = pet * 50
    vt= valor+preço+custo
    print('O valor do transporte para os itens acima é de R$',vt)

    resposta = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    while resposta not in "SN":
        resposta = str(input("ERRO! Responda apenas S ou N ")).strip().upper()[0]
    if resposta == "N":
        break
print('-' * 40)
print('Agradecemos a preferência!!!')
print('-' * 40)