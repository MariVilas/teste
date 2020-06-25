resposta = 'SN'
cont=('Corinthians','Palmeiras','Santos','Flamengo','Grêmio',
      'Chapecoense','Internacional','Curitiba','Atlético Mineiro',
      'Cruzeiro','São Paulo','Vasco','Bahia',
      'Fluminense','Portuguesa','Náutico',
      'Atlético Paranaense','Paissandu','Botafogo',
      'Goiás','Fortaleza')
print(f'Os cinco primeiros colocados são :{cont[:5]}')
print(f'Os quatro últimos colocados são :{cont[17:]}')
print(f'Os times em ordem alfabética :{sorted(cont)}')
print(f'A posição na tabela do time Chapecoense é :{cont.index("Chapecoense")}')
