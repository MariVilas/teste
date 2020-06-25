from time import sleep
resp = 'SN'
dado={}
while True:
  dado['nome']=str(input('Nome: '))
  dado['nascimento']=str(input('Ano de Nascimento: '))
  dado['CTPS']=int(input('CTPS: '))
  dado['contratação']=int(input('Ano de Contratação: '))
  dado['salário']=int(input('Salário: '))

  dado['aposentadoria']= dado['contratação']+35
  resp = str(input('Quer continuar?[S/N]')).upper().strip()[0]
  if resp == 'N':
     break

print("CAL\n")
sleep(1)
print("CU\n")
sleep(1)
print("LANDO!!!\n")
print(dado)
print("-=" * 20)
print("-=" * 20)
print("-=" * 20)
print('Finalizando!!!')
print("-=" * 20)