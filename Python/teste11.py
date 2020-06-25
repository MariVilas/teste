import math
from time import sleep

lista = ("Binário", "Octal", "Hexadecimal")

numero=int(input('Entre com um número:'))

perguntar = int(input('''Escolha uma opcao para sua conversão: 

[1] Binário
[2] Octal
{3} Hexadecimal

Digite sua escolha: '''))

print("CAL\n")
sleep(1)
print("CU\n")
sleep(1)
print("LANDO!!!\n")



if perguntar == 1:
     print('{}  Convertido para Binário é igual a  {}'.format(numero,bin(numero)))
elif perguntar ==2:
     print('{}  Convertido para Octal é igual a  {}'.format(numero,oct(numero)))
elif perguntar == 3:
    print('{}   Convertido para Hexadecimal é igual a {}'.format(numero,hex(numero)))

