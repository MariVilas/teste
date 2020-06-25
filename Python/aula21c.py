print('-'*30)
print('-'*30)

def leiaInt(msg = ''):
    while True:
        valor = str(input(msg))
        if valor.isnumeric():
            break
        else:
            print('ERRO! Digite um número inteiro válido!')
    return valor


#PROGRAMA PRINCIPAL
num = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {num}')