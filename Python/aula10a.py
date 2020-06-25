import random

computador=random.randint(0,5)

print('Vou pensar em um número...')
jogador=int(input('Tente advinhar:'))
if jogador==computador:
    print('Você Acertou!!!')
else:
    print('Você Perdeu!', 'Eu pensei no número',computador, 'e não no número',jogador)