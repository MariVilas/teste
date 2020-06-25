def leiaint(txt):
    while True:
        num = input(txt)
        try:
            num = int(num)
        except KeyboardInterrupt:
            print('ERRO!! O usuário prefiriu não informar os dados')
            num = 0
        except:
            print('ERRO!! Digite um número valido!!!')
        else:
            return num
            break

def leiafloat(txt):
    while True:
        num = input(txt)
        try:
            num = float(num)
        except KeyboardInterrupt:
            print('ERRO!! O usuário prefiriu não informar os dados')
            num = 0
        except:
            print('ERRO!! Digite um número valido!!!')
        else:
            return num
            break

def parar(Resp):
  while Resp in 'Ss':
   if Resp=='Nn':
     break


print('-'*30)
Resp='SN'
while True:
 n = leiaint('digite um numero: ')
 n1 = leiafloat('digite um numero real: ')
 print(f'Foram digitados os numeros {n} e {n1}')
 Resp = str(input('Quer continuar?[S/N]')).upper().strip()[0]
 if Resp == 'N':
     break
print('FIM!!!')
