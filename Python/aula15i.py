resp= 'SN'
while True:
    print("-=" * 20)
    print("Seja bem-vindo ao banco do Zubiano!\n\n")
    print("-=" * 20)
    numero = int(input('Valor para sacar [10-600]R$ '))

    cem = int(numero / 100)
    numero = numero - (cem * 100)

    cinquenta = int(numero / 50)
    numero = numero - (cinquenta * 50)

    dez = int(numero / 10)
    numero = numero - (dez * 10)

    cinco = int(numero / 5)
    numero = numero - (cinco * 5)

    um = numero

    print('Notas R$100,00 = ', cem)
    print('Notas R$ 50,00 = ', cinquenta)
    print('Notas R$ 10,00 = ', dez)
    print('Notas R$  5,00 = ', cinco)
    print('Notas R$  1,00 = ', um)
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