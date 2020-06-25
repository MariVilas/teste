nome= list()
nota1= list()
nota2= list()
pessoas= list()
media= list()
pesssoasaprovadas=list()
pessoasreprovadas=list()
while True:
       nome = str(input('Nome: '))
       notaa = float(input('Nota: '))
       notab = float(input('Nota: '))
       stop = str(input('Deseja continuar [S/N]: ')).upper().strip()
       if stop == 'N':
           break
       pessoas.append(nome)
       nota1.append(notaa)
       nota2.append(notab)
       mediaa= (notaa+notab)//2
       media.append(mediaa)
       if mediaa < 7:
        pessoasreprovadas.append(nome)
       elif mediaa >7:
        pesssoasaprovadas.append(nome)

print(f'Alunos{pessoas}')
print(f'Notas {nota1,nota2}')
print(f' Média{media}')
print(f'As pessoas APROVADAS foram {pesssoasaprovadas} Parabéns!')
print(f'As pessoas REPROVADAS foram {pessoasreprovadas} Estude para Recuperação!')
