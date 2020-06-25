resp= 'SN'
while True:
    valores= list()
    for cont in range(0,5):
         valores.append(int(input('Entre com um valor:')))
    for c,v in enumerate(valores):
        print(f'Na posição {c} encontrei o valor {v}!')
    print(f'O maior número é:{max(valores)}')
    print(f'O menor número é:{min(valores)}')

    resp = str(input('Quer continuar?[S/N]')).upper().strip()[0]
    if resp == 'N':
        print("-=" * 20)
        print("-=" * 20)
        print("-=" * 20)
        print('Finalizando!!!')
        print("-=" * 20)
        print("-=" * 20)
        print("-=" * 20)