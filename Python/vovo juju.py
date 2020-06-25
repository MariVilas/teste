import random
from time import sleep
resposta='SN'
while True:

    print('-' * 40)
    print(f'{"Cartoon Network":^40}')
    print(f'{"A frase de hoje da Vovó Juju para você é:":^40}')
    print('-' * 40)
    computador = random.randint(0,10)

    print("Irmão\n")
    sleep(1)
    print("do\n")
    sleep(1)
    print("Jorel!!!\n")




    if computador == 0:
      print('-' * 40)
      print("Isso é a escola do Crime!")
      print('-' * 40)

    elif computador == 1:
     print('-' * 40)
     print("Come bem, o Abacate!")
     print('-' * 40)

    elif computador == 2:
     print('-' * 40)
     print("Come mingau de aveia, pra fazer cocô bonito!")
     print('-' * 40)

    elif computador == 3:
     print('-' * 40)
     print("Ana Catarina, que nome feio!")
     print('-' * 40)

    elif  computador == 4:
     print('-' * 40)
     print("Olha que lindo, tá se alimentando!")
     print('-' * 40)

    elif computador == 5:
     print('-' * 40)
     print("Eu sempre quis conhecer o fundo do mar!")
     print('-' * 40)

    elif computador == 6:
     print('-' * 40)
     print("Pisou na minha mudinha!")
     print('-' * 40)

    elif computador == 7:
     print('-' * 40)
     print("Que bolo bonito, não é pra comer é pra ficar olhando!")
     print('-' * 40)

    elif computador == 8:
     print('-' * 40)
     print("Ao infinito e além, bem!")
     print('-' * 40)

    elif computador == 9:
     print('-' * 40)
     print("Passa abacate no cabelo, pra ele crescer e ficar bonito!")
     print('-' * 40)

    elif computador == 10:
     print('-' * 40)
     print("Come farofa,come!")
     print('-' * 40)

    resposta = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    while resposta not in "SN":
        resposta = str(input("ERRO! Responda apenas S ou N ")).strip().upper()[0]
    if resposta == "N":
        break
print('-' * 40)
print('Assiste irmão do Jorel, no Cartoon Network Bem!')
print('-' * 40)