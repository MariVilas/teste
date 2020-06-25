p=(int(input('Entre com um número:')),
   int(input('Entre com um número:')),
   int(input('Entre com um número:')),
   int(input('Entre com um número:')))

print(f'Você digitou os valore{p}')
print('O número 9 apareceu:',p.count(9))
print('O número 3 apareceu na posição:',p.index(3)+1)
print('Os números pares são:',end='')
for n in p:
    if n%2==0:
        print(n,end='')
