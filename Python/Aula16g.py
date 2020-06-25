palavras=('Sapato','Camisa','Blusa',
          'Shorts','Camiseta','Sapatilha',
          'Calça','Tenis','Jaqueta','Blazer',
          'Bermuda','Bota','Chinelo')

for p in palavras:
 print(f'\nNa palavra {p.upper()} temos:')
 for letra in p:
    if letra.lower() in 'aeiou':
      print('Vogal:',letra)

 for vogal in p:
     if vogal.lower() in 'bcdfghjklmnpqrstvxz':
         print('Consoante:',vogal)
