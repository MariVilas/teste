from time import sleep
resp = 'SN'
dado={}
while True:
  dado['nome']=str(input('Nome do Jogador: '))
  dado['partidas']=int(input('Partidas disputadas: '))
  dado['gol']=int(input('Gols por Partida: '))
  dado['aproveitamento']= dado['partidas']* dado['gol']
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