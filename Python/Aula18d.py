nome= list()
nota= list()
pessoas= list()
pesssoasaprovadas=list()
pessoasreprovadas=list()
while True:
       nome = str(input('Nome: '))
       nota = float(input('Nota: '))
       pessoas.append(nome)
       if nota < 7:
        pessoasreprovadas.append(nome)
       elif nota >7:
        pesssoasaprovadas.append(nome)
       stop = str(input('Deseja continuar [S/N]: ')).upper().strip()
       if stop == 'N':
           break
print(f'Foram cadastradas {len(pessoas)} pessoas')
print(f'As pessoas APROVADAS foram {pesssoasaprovadas} Parabéns!')
print(f'As pessoas REPROVADAS foram {pessoasreprovadas} Estude para Recuperação!')
