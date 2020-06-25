resposta='SN'
while True:

    print('-' * 40)
    print(f'{"Estações do Ano":^40}')
    print('-' * 40)
    valor =(int(input('Entre com a temperatura atual:')))
    if valor <=15:
     print('Inverno')
    if valor >= 16 :
     print('Outono')
    if valor <=20:
    print('Outono')
    if valor >= 21:
      print('Primavera')
    if valor >= 30:
     print('Primavera')
    if valor > 30:
     print('Verão')



    resposta = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    while resposta not in "SN":
        resposta = str(input("ERRO! Responda apenas S ou N ")).strip().upper()[0]
    if resposta == "N":
        break
print('-' * 40)
print('Aproveite seja qual for a estação!')
print('-' * 40)




