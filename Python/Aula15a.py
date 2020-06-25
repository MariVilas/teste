soma = quantidade =  0

while True:
  num = int(input('Entre com um número:'))
  if num ==999:
      break
  soma += num
  quantidade += 1
print(f'Você digitou {quantidade} números e a Soma foi {soma}')