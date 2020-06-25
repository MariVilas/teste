s = int(input('Entre com o seu salário:'))

if s > 1250:
    a=s*0.10
    s1= s+a
    print('Esse é seu Aumento:',a)
    print('Seu novo salário é:',s1)
else:
    s<=1250
    b=s*0.15
    s2=s+b

    print('Esse é o seu Aumento:',b)

    print('Seu novo salário é:',s2)

