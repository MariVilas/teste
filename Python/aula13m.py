maior = 0
menor = 1000
for c in range(1, 6):
    n = int(input('Digite o peso da {} pessoa: '. format(c)))
    if n > maior:
        maior = n
    if n < menor:
        menor = n
print('O menor peso é {}Kg e o maior peso é {}Kg'.format(menor, maior))