resp='S'
soma = quantidade = media= 0

while resp in 'Ss':
  num = int(input('Entre com um número:'))
  soma+= num
  quantidade +=1

  resp=str(input('Quer continuar?[S/N]')).upper().strip()[0]
media=num//quantidade
print(f'Você digitou {quantidade} números e a Média foi {media}')
