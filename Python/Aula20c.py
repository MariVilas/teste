from time import sleep


def linha():
    print('-=' * 20)


def contador(a, b, c):
    if c < 0:
        c = c * -1
    elif c == 0:
        c = 1
    print(f'Contagem de {a} até {b} de {c} em {c}')
    s = a
    if a < b:
        while s <= b:
            sleep(0.3)
            print(s, end=' ')
            s += c
        print('FIM')
    else:
        while s >= b:
            sleep(0.3)
            print(s, end=' ')
            s -= c
        print('FIM')


# Programa principal
linha()
contador(1, 10, 1)
linha()
contador(10, 0, 2)
linha()
print('Personalize a contagem')
início = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
linha()
contador(início, fim, passo)


