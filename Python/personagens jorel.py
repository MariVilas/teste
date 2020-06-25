import random
from time import sleep
resposta='SN'
while True:

    print('-' * 40)
    print(f'{"Cartoon Network":^40}')
    print(f'{"Qual personagem do desenho você é:":^40}')
    print('-' * 40)
    computador = random.randint(0,10)

    print("Irmão\n")
    sleep(1)
    print("do\n")
    sleep(1)
    print("Jorel!!!\n")




    if computador == 0:
      print('-' * 40)
      print("Irmão do Jorel")
      print('-' * 40)

    elif computador == 1:
     print('-' * 40)
     print("Jorel!")
     print('-' * 40)

    elif computador == 2:
     print('-' * 40)
     print("Vovó Juju")
     print('-' * 40)

    elif computador == 3:
     print('-' * 40)
     print("Ana Catarina")
     print('-' * 40)

    elif  computador == 4:
     print('-' * 40)
     print("Lara")
     print('-' * 40)

    elif computador == 5:
     print('-' * 40)
     print("Vovó Gigi")
     print('-' * 40)

    elif computador == 6:
     print('-' * 40)
     print("Gesonel")
     print('-' * 40)

    elif computador == 7:
     print('-' * 40)
     print("Nico")
     print('-' * 40)

    elif computador == 8:
     print('-' * 40)
     print("Fabrício")
     print('-' * 40)

    elif computador == 9:
     print('-' * 40)
     print("Danúbio")
     print('-' * 40)

    elif computador == 10:
     print('-' * 40)
     print("Yuki")
     print('-' * 40)

    resposta = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    while resposta not in "SN":
        resposta = str(input("ERRO! Responda apenas S ou N ")).strip().upper()[0]
    if resposta == "N":
        break
print('-' * 40)
print('Assiste irmão do Jorel, no Cartoon Network Bem!')
print('-' * 40)