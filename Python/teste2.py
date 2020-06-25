import random



j1 =input('(1° aluno) Digite seu nome: ')
j2 =input('(2° aluno) Digite seu nome: ')
j3 =input('(3° aluno) Digite seu nome: ')
j4=input('(4° aluno)Digite seu nome:')

s= random.randint(1,4)
if s == 1:
    print('Parabéns',j1,'Você Ganhou!!')
elif s == 2:
    print('Parabéns',j2,'Você Ganhou!!')
elif s  == 3:
    print('Parabéns', j3, 'Você Ganhou!!')
elif s == 4:
    print('Parabéns',j4,'Você Ganhou!!')

