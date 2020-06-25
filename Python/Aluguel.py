import random
from time import sleep
resposta='SN'
while True:

    print('-' * 40)
    print(f'{"Imobiliária do Zubiano":^40}')
    print(f'{"Calcule a multa de quebra de contrato":^40}')
    print('-' * 40)
    valor =(int(input('Entre com o valor do Aluguel:')))
    tempo = (int(input('Entre com a quantidade de tempo que falta para o término do contrato(36 meses):')))
    print("Cal\n")
    sleep(1)
    print("cu\n")
    sleep(1)
    print("lando!!!\n")

    multa1= valor*3/36
    multa2= multa1*tempo

    print('O valor da multa é: R$',multa2)
    resposta = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    while resposta not in "SN":
        resposta = str(input("ERRO! Responda apenas S ou N ")).strip().upper()[0]
    if resposta == "N":
        break
print('-' * 40)
print('Obrigada por utilizar nossos serviços!')
print('-' * 40)