resp='S N'
cem=cinquenta=vinte=dez=cinco=dois=0
while True:
    print("-=" * 20)
    print("-=" * 20)
    print("-=" * 20)
    print('**Banco do Zubiano**')
    lista = ("10", '20','50','100')

    perguntar = int(input('''Escolha uma opção: 

        [0] R$10
        [1] R$20
        [2] R$50
        [3} R$100
        
        Digite sua escolha: '''))

    if perguntar == 0:
       dez+=1
       print("-=" * 20)
       print('O saque em nota de dez:', dez)
       print("-=" * 20)
       resp = str(input('Quer continuar?[S/N]')).upper().strip()[0]

    if resp == 'N':
           break
    elif perguntar == 1:
       vinte+=1
       print("-=" * 20)
       print('O saque em nota de vinte:', vinte)
       print("-=" * 20)
       resp = str(input('Quer continuar?[S/N]')).upper().strip()[0]

    if resp == 'N':
           break
    elif perguntar ==2:
       cinquenta+=1
       print("-=" * 20)
       print('O saque em nota de cinquenta:', cinquenta)
       print("-=" * 20)
       resp = str(input('Quer continuar?[S/N]')).upper().strip()[0]

    if resp == 'N':
           break
    elif perguntar==3:
     cem+=1
     print("-=" * 20)
     print('O saque em nota de cem:', cem)
     print("-=" * 20)

     resp = str(input('Quer continuar?[S/N]')).upper().strip()[0]

     if resp == 'N':
             break
print("-=" * 20)
print("-=" * 20)
print("-=" * 20)
print('Obrigada por utilizar nossos serviços!!!')
print("-=" * 20)
print("-=" * 20)
print("-=" * 20)