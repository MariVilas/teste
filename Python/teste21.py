resp= 'SN'
valores= list()
vogal=list()
consoante= list()
while True:
    valores.append(str(input('Entre com um valor:')))
    resp = str(input('Quer continuar?[S/N]')).upper().strip()[0]
    if resp == 'N':
        break
if valores in 'aeiou':
  print(vogal, end=' ')
elif valores in 'bcdfghjklmnpqrstvxz':
  print(consoante, end=' ')

print("-=" * 20)
