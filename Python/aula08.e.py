from random import sample

j1 = str(input('(1° Aluno) Digite seu nome: '))
j2 = str(input('(2° Aluno) Digite seu nome: '))
j3 = str(input('(3° Aluno) Digite seu nome: '))
j4 = str(input('(4° Aluno) Digite seu nome: '))

s= j1,j2,j3,j4
sort = sample(s,len(s))


print('Sorteio:',sort)