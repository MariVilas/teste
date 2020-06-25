resp = 'SN'
while True:

    print("-=" * 20)
    print("Números por Extenso!")
    print("-=" * 20)
    numeros = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)
    perguntar = int(input('Escolha com um número de 0 a 20:'))

    if perguntar == 0:
     print('O valor digitado foi Zero')
     break
    if perguntar == 1:
     print('O valor digitado foi Um')
     break
    if perguntar == 2:
     print('O valor digitado foi Dois')
     break
    if perguntar == 3:
     print('O valor digitado foi Três')
     break
    if perguntar == 4:
     print('O valor digitado foi Quatro')
     break
    if perguntar == 5:
     print('O valor digitado foi Cinco')
     break
    if perguntar == 6:
     print('O valor digitado foi Seis')
     break
    if perguntar == 7:
     print('O valor digitado foi Sete')
     break
    if perguntar == 8:
     print('O valor digitado foi Oito')
     break
    if perguntar == 9:
      print('O valor digitado foi Nove')
      break
    if perguntar == 10:
     print('O valor digitado foi Dez')
     break
    if perguntar == 11:
     print('O valor digitado foi Onze')
     break
    if perguntar == 12:
     print('O valor digitado foi Doze')
     break
    if perguntar == 13:
     print('O valor digitado foi Treze')
     break
    if perguntar == 14:
     print('O valor digitado foi Quatorze')
     break
    if perguntar == 15:
     print('O valor digitado foi Quinze')
     break
    if perguntar == 16:
     print('O valor digitado foi Dezesseis')
     break
    if perguntar == 17:
     print('O valor digitado foi Dezessete')
     break
    if perguntar == 18:
     print('O valor digitado foi Dezoito')
     break
    if perguntar == 19:
     print('O valor digitado foi Dezenove')
     break
    if perguntar == 20:
     print('O valor digitado foi Vinte')
     break
    if perguntar != numeros:
     print('Tente novamente!')
else:
 resp = str(input('Quer continuar?[S/N]')).upper().strip()[0]
if resp =='N':
 print('Finalizando!!!')
 print("-=" * 20)
 print("-=" * 20)


