resp= 'SN'
valores= list()
while True:
    n=int(input('Entre com um número:'))
    if n not in valores:
        valores.append(n)
        print('Valor Adicionado com sucesso')
    else:
       print(f'Valor Duplicado!')
    resp = str(input('Quer continuar?[S/N]')).upper().strip()[0]
    if resp == 'N':
        break
print("-=" * 20)
print("-=" * 20)
print("-=" * 20)
print('Finalizando!!!')
print("-=" * 20)
print("-=" * 20)
print("-=" * 20)