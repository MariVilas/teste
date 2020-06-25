resp= 'SN'
valores= list()
while True:
    valores.append(int(input('Entre com um valor:')))
    resp = str(input('Quer continuar?[S/N]')).upper().strip()[0]
    valores.sort(reverse=True)
    if resp == 'N':
        break
print(f'O quantidade de números digitados foi:{len(valores)}')
print(valores)
if 5 in valores:
 print('Encontrei o número 5!!!')
 print("-=" * 20)
 print("-=" * 20)
 print("-=" * 20)
 print('Finalizando!!!')
 print("-=" * 20)
 print("-=" * 20)
 print("-=" * 20)
