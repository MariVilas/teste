from datetime import date
ctps = dict()
ano = date.today().year
while True:
    ctps['nome'] = str(input('Nome: '))
    ctps['Idade'] = int(input('Ano de nascimento: '))
    ctt = ctps['Idade']
    ctps['Idade'] = ano - ctps['Idade']
    ctps['ctps'] = int(input('Carteira de trabalho [0 não tem] '))
    if ctps['ctps'] == 0:
        for k, v in ctps.items():
            print(f'  - {k} tem o valor {v}')
        break
    else:
        ctps['contratação'] = int(input('Ano de contratação: '))
        ctps['salario'] = float(input('Salario: R$'))
        ctps['aposentadoria'] = ctps['contratação'] -  ctt + 35
        for k, v in ctps.items():
            print(f'  - {k} tem o valor {v}')
        break