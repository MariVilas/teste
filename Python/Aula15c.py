from random import randint
from time import sleep
resp='S'
jogo  = resultado = 0
while resp in 'Ss':
  lista = ("PAR","ÍMPAR")

  computador = randint(0, 1)

  perguntar = int(input('''Escolha uma opcao para se jogar: 

  [0] PAR
  [1] ÍMPAR


  Digite sua escolha: '''))

  print("ÍMPAR\n")
  sleep(1)
  print("OU\n")
  sleep(1)
  print("PAR!!!\n")

  print("-=" * 20)
  print("O computador escolheu: {}".format(lista[computador]))
  print("O jogador escolheu: {}".format(lista[perguntar]))
  print("-=" * 20)

  if computador == 0:
    if perguntar == 0:
      print("Empate!")
      if computador == 1:
        if perguntar == 1:
          print("Empate!")
  resultado += 1
  resp = str(input('Quer continuar?[S/N]')).upper().strip()[0]
print(resultado)


