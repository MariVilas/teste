resposta='SN'
compras=list()
preços=list()
listagem=list()
while True:
    print('-'*40)
    print(f'{"Cupom Fiscal":^40}')
    print(f'{"Lojas Renner/SA":^40}')
    print('-'*40)
    descrição=input(str('Entre com a descrição da peça:'))
    compra=input(str('Entre com o valor da peça:'))
    compras.append(descrição)
    listagem.append(compra)
    resp = ' '
    resposta = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    while resposta not in "SN":
        resposta = str(input("ERRO! Responda apenas S ou N ")).strip().upper()[0]
    if resposta == "N":
        break
print(f'Itens {(descrição)}')
print(f'Preços {sum(compra)}')
