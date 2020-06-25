pares= list()
impares= list()
for c in range(0, 5):
 num = int(input('Entre com um número: '))
 if num % 2 == 0:
  pares.append(num)
 elif  num % 2 == 1:
  impares.append(num)

print(f'Os valores pares digitados foram: {pares}.')
print(f'Os valores ímpares digitados foram: {impares}.')