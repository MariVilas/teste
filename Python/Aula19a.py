media = {}
resp= 'SN'
while True:
    media['nome']=str(input('Nome: '))
    media['nota']=float(input('Entre com a Média: '))
    if media['nota'] >=7 :
     media['resultado'] = 'aprovado'
    else:
     media['resultado'] = 'reprovado'
    print('=-' * 25)
    print(media)
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if resp == 'N':
      break

print('=-'*25)
print('=-'*25)
print('Finalizando!!!')