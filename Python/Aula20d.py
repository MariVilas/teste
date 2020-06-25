print('-'*30)
resp= 'S'
def linha():
    print('-=' * 20)
def maior():
    list = []
    list.append(int(input('Insira um valor: ')))
    list.append(int(input('Insira um valor: ')))
    list.append(int(input('Insira um valor: ')))
    list.append(int(input('Insira um valor: ')))
    m = max(list)
    print(f'O maior valor da lista: {list}\nO MAIOR VALOR É O: {m}')




while resp in 'Ss':
    linha()
    maior()
    resp = str(input('Quer continuar?[S/N]')).upper().strip()[0]
    linha()