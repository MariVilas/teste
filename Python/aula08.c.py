import math

angulo= int(input('Entre com o ângulo que você deseja:'))

seno= math.sin(math.radians(angulo))
cosseno= math.cos(math.radians(angulo))
tangente= math.tan(math.radians(angulo))

print('O valor do ângulo {}  tem o Seno: {:.2f} o Cosseno {:.2f} e a Tangente {:.2f}'.format(angulo,seno,cosseno,tangente))
