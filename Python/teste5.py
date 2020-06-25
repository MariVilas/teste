resp= 'S'

while resp in 'Ss':


    k = int(input('Entre com a quantidade de Km a serem percorridos:'))

    c1 = k//15
    c1a= k//12
    c2 = k//12
    c2a= k//10
    c3 = k//10
    c3a= k//8

    print(' O Gasto de combustível estimado para um carro 1.0 utilizando gasolina é de:',c1,'l e',c1a,'l utilizando Etanol')
    print(' O Gasto de combustível estimado para um carro 1.6  utilizando gasolina é de:',c2, 'l  e',c2a,'l  utilizando Etanol')
    print(' O Gasto de combustível estimado para um carro 2.0  utilizando gasolina é de:',c3,'l  e',c3a,'l  utilizando Etanol')

    resp = str(input('Quer continuar?[S/N]')).upper().strip()[0]
    k
    print("-=" * 20)
    print("-=" * 20)
    print("-=" * 20)