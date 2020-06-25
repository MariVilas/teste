def escreva(txt):
    print('~' * (len(txt) + 6))
    print(f'   {txt}   ')
    print('~' * (len(txt) + 6))

escreva(str(input('Insira texto: ')))