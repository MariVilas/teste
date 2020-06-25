resp= 'SN'
valores= list()
par=list()
impar= list()
while True:
    valores.append(int(input('Entre com um valor:')))
    resp = str(input('Quer continuar?[S/N]')).upper().strip()[0]
    if resp == 'N':
        break
for i, v in enumerate(valores):
 if v % 2 == 0:
  par.append(v)
 elif v % 2 == 1:
     impar.append(v)

print("-=" * 20)
print(f'A lista completa de números é:{valores}')
print(f'A lista  de números pares é:{par}')
print(f'A lista  de números ímpares é:{impar}')



