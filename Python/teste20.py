lista = []
flag = False

for x in range(8):

    tamanho = len(lista)

    n = int(input("Digite um número inteiro: "))

    if( tamanho > 0 ):

        for y in range( tamanho ):

            if ( n <= lista[y] ):

                lista.insert( y, n )

                flag = True

                break

    if((x == 0) or (flag == False)):

        lista.append( n )

    else:

        flag = False

print(lista)