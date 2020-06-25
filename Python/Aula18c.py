from  random import randint
jogo= list()
lista= list()
print("-=" * 20)
print('Bolão da Mega')
print("-=" * 20)
num = int(input('Entre com um número de jogos: '))
total=1
while total <=num:
    cont = 0
    while True:
        computador = randint(1, 60)
        if computador not in jogo:
         jogo.append(computador)
        cont+=1
        if cont >=6:
             break
    jogo.sort()
    lista.append(jogo[:])
    jogo.clear()
    total+=1
print(f'Os Jogos Sorteados foram: {lista}')
