resp= 'S'

while resp in 'Ss':
  sexo=int(input('''Entre com seu sexo:

  [0] Masculino
  [1] Feminino
  [2] Transgênero
  [3] Não Binário

  Digite sua escolha: '''))

  if sexo == 0:
    print("Você é um LIXO!")
  elif sexo == 1:
    print("Força Mana")
  elif sexo == 2:
    print("Se orgulhe de você!!!!")
  else:
    print("A diversidade faz o mundo!!!")


  resp = str(input('Quer continuar?[S/N]')).upper().strip()[0]
  sexo
  print("-=" * 20)
  print("-=" * 20)
  print("-=" * 20)