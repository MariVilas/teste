import locale
locale.setlocale(locale.LC_MONETARY, 'Portuguese_Brazil.1252')

def metade(preço=0):
    return preço/2


def dobro(preço=0):
    return preço*2


def aumentar(preço=0, taxa=0):
    return preço + (preço * taxa/100)


def reduzir(preço=0, taxa=0):
    return preço - (preço * taxa/100)


def moeda(preço):
    return {locale.currency(preço)}

