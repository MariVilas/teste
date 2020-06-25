import random
from time import sleep
resp='S N'
vitoria=0
while True:
    nome = str(input ("Introduza seu nome: "))
    b=0
    computador = random.randint (0,10)
    utilizador = str(input ("Você escolhe par ou impar: "))

    if utilizador == "par":
       par = utilizador
       impar = computador
    elif utilizador == "impar":
       impar = utilizador
       par = computador
    else:
       b=1
       print ("ERRO")

    if b!=1:

       numero = int(input("Digite o numero: (0/10) "))
       computador = random.randint (1,10)
       print("-=" * 20)
       print("PAR\n")
       sleep(1)
       print("OU\n")
       sleep(1)
       print("IMPAR!!!\n")

       print("-=" * 20)
       print ("\nComputador escolheu: ",computador)
       print (nome," escolheu: ",numero)
       total = numero + computador
       print ("A Soma é: ",total)
       computador="0"
       if total%2==0:
           print ("O Resultado é: Par")
           computador="par"
       else:
           print ("O Resultado é: Impar")
           computador="impar"
       if utilizador == "par" and computador=="par":
           print  ("Ganhou o : ",nome)
           vitoria+=1
       if utilizador == "impar" and computador=="impar":
           print  ("Ganhou  : ",nome)
           vitoria+=1
       else:
         print("Ganhou o Computador")


    resp = str(input('Quer continuar?[S/N]')).upper().strip()[0]
    if resp == 'N':
        break
print('Jogo Finalizado!!!','Você venceu:',vitoria)