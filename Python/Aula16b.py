resposta = 'SN'
cont=('Zero','Um','Dois','Três','Quatro',
      'Cinco','Seis','Sete','Oito',
      'Nove','Dez','Onze','Doze',
      'Treze','Quatorze','Quinze',
      'Dezesseis','Dezessete','Dezoito',
      'Dezenove','Vinte')
while True:

 num=int(input('Entre com um número de 0 a 20:'))
 if 0 <= num <= 20 :
  print(f'Você digitou o número :{cont[num]}')
  resposta = str(input('Quer continuar?[S/N]')).upper().strip()[0]
  if resposta == 'N':
      print('Finalizando!!!')
      print("-=" * 20)
      print("-=" * 20)
      break
 else:
  print('Tente Novamente.',end='')
  resposta=str(input('Quer continuar?[S/N]')).upper().strip()[0]
 if resposta == 'N':
  print('Finalizando!!!')
  print("-=" * 20)
  print("-=" * 20)
  break
