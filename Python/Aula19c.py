from time import sleep
from random import randint

listaDePontuações = []
listaDeJogadores = []
for c in range(1, 5):
    listaDeJogadores.append({'número do jogador': c, 'número sorteado': randint(1, 6)})
    print(f'o {c}º jogador sorteu o número {listaDeJogadores[c - 1]["número sorteado"]}')
    sleep(1)
for c in range (0, 4):
    listaDePontuações.append(listaDeJogadores[c]['número sorteado'])
listaDePontuações.sort()
for c in range(1, listaDePontuações.__len__() + 1):
    print(f'{c}º jogador: tirou {listaDePontuações[listaDePontuações.__len__() - c]}')
    sleep(1)