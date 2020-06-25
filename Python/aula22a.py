import locale
locale.setlocale(locale.LC_MONETARY, 'Portuguese_Brazil.1252')

def metade(n=0):
    n=n/2
    print(f'O valor da metade do valor é R$ {n}')

def dobro(n=0):
    n=n*2
    print(f'O  valor do dobro do valor é R$ {n}')

def triplo(n=0):
    n=n*3
    print(f'O valor do triplo do valor é R$ {n}')

def desconto(n=0):
    d= n*10/100
    n= n-d
    print(f'O  valor com 10% de desconto é R$ {n}')

def acrescimo(n=0):
    d = n * 10/100
    n = n + d
    print(f'O valor com 10% de acréscimo é R$ {n}')

def moeda(n=0):
    return {locale.currency(n)}






