from  random import randint
from time import sleep
def sorteando(lista):
    from random import randint
    for i in range(0,5):
        num =  randint(0,100)
        lista.append(num)


def somapar(lista):
    soma = 0
    for i in lista:
        if i%2 == 0:
            soma += i
    print(soma)

lista = []
sorteando(lista)

print(f'Sorteando 5 valores: ', end='')
for c in lista:
    print(c, end=' ')
print('PRONTO!!!')

print('A soma dos valores pares é ', end='')
somapar(lista)

