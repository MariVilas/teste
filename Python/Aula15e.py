import random
resp='S N'
adultos=0
homens=0
mulheres=0
jovens=0
while True:
    idade=int(input('Entre com a sua idade:'))
    lista = ("Masculino",'Feminino')

    perguntar = int(input('''Escolha uma opção: 

    [0] Masculino
    [1] Feminino
     Digite sua escolha: '''))

    if perguntar == 0:
       homens+=1
    elif perguntar == 1:
       mulheres+=1
    else:
       print ("ERRO")

    if idade > 18:
       adultos+=1
    elif idade <20 and perguntar==1:
       jovens+=1
    else:
       print ("ERRO")


    resp = str(input('Quer continuar?[S/N]')).upper().strip()[0]
    if resp == 'N':
        break
print("-=" * 20)
print("-=" * 20)
print("-=" * 20)
print('O número de maiores de 18 anos é de:',adultos)
print('O número de homens cadastrados é de:',homens)
print('O número de mulheres cadastradas é de:',mulheres)
print('O número de mulheres com menos de 20 anos é de :',jovens)
print("-=" * 20)
print("-=" * 20)
print("-=" * 20)