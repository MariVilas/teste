from random import randint
from time import sleep
computador = randint(0, 11)
print('Vou pensar em um número... Você consegue advinhar???')

print("PEN\n")
sleep(1)
print("SAN\n")
sleep(1)
print("DO!!!\n")

print("-=" * 20)

acertou= False
palpite= 0
while not acertou:
    perguntar = int(input('''Escolha um número de 0 a 10 para jogar: 

    Digite sua escolha: '''))
    palpite+=1
    if computador == perguntar:
       acertou=True
print('Você Acertou!!!Com {} tentativas'.format(palpite))






