resp='SN'
nome= list()
peso= list()
pessoas= list()
pesssoaspesadas=list()
pessoasleves=list()
while True:
       nome = str(input('Nome: '))
       peso = float(input('Peso: '))
       pessoas.append(nome)
       if peso > 100:
        pesssoaspesadas.append(nome)
       elif peso < 60:
        pessoasleves.append(nome)
       stop = str(input('Deseja continuar [S/N]: ')).upper().strip()
       if stop == 'N':
           break
print(f'Foram cadastradas {len(pessoas)} pessoas')
print(f'As pessoas mais pesadas foram {pesssoaspesadas} com peso acima de 100 Kg,procure um médico!')
print(f'As pessoas mais leves foram {pessoasleves} com peso abaixo de 60 Kg,mantenha sua saúde!')
