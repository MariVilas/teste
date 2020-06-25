import math
pessoa = dict()
idad = list()
mulher = list()
soma = media = 0
total= list()
homem=list()
catolico=list()
espirita=list()
evangelico=list()
branco=list()
negro= list ()
pardo=list ()
while True:
    print('-' * 40)
    print(f'{"IBGE/BRASIL":^40}')
    print(f'{"CENSO 2019":^40}')
    print('-' * 40)
    pessoa['nome'] = str(input("Nome: "))
    pessoa['sexo'] = str(input("Sexo: [M/F] ")).strip().upper()[0]
    while pessoa['sexo'] not in "MF":
        pessoa['sexo'] = str(input("ERRO! Por favor, digite apenas M ou F ")).strip().upper()[0]
    if pessoa['sexo'] == "M":
        homem.append(pessoa['nome'])
    if pessoa['sexo'] == "F":
        mulher.append(pessoa['nome'])
    pessoa['idade'] = int(input("Idade: "))
    soma += pessoa['idade']
    idad.append(pessoa.copy())
    total.append(pessoa.copy())
    lista = ("Católico", "Espírita", "Evangélico")

    perguntar = int(input('''Escolha uma opcao para sua religião: 

        [0] Católico
        [1] Espírita
        [2] Evangélico
         Digite sua escolha: '''))
    if perguntar == 0:
     catolico.append(pessoa.copy())
    if perguntar == 1:
     espirita.append(pessoa.copy())
    if perguntar == 2:
     evangelico.append(pessoa.copy())

    lista = ("Branco", "Negro", "Pardo")

    perguntar = int(input('''Escolha uma opcao para sua etnia: 

            [0] Branco
            [1] Negro
            [2] Pardo
             Digite sua escolha: '''))
    if perguntar == 0:
        branco.append(pessoa.copy())
    if perguntar == 1:
        negro.append(pessoa.copy())
    if perguntar == 2:
        pardo.append(pessoa.copy())

    resposta = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    while resposta not in "SN":
        resposta = str(input("ERRO! Responda apenas S ou N ")).strip().upper()[0]
    if resposta == "N":
        break
print("-=" * 30)
print(f"A) Ao todo foram cadastradas {len(total)} pessoas")
media = soma / len(idad)
print(f" B) Os praticantes da religião Católica são: {len(catolico)} ")
print(f" C) Os praticantes da religião Espírita são: {len(espirita)}")
print(f" D) Os praticantes da religião Evangélica são: {len(evangelico)}")
print(f" E) Os cidadãos pertencentes a etnia Branca são: {len(branco)} ")
print(f" F) Os cidadãos pertencentes a etnia Negra são: {len(negro)}")
print(f" G) Os cidadãos pertencentes a etnia Parda são: {len(pardo)}")
print(f" H) A média de idade é de {media:5.2f} anos")
print(f" I) As mulheres cadastradas foram: {mulher}")
print(f" J) Os homens cadastrados foram: {homem}")
print('-' * 40)
print(f'{"IBGE/BRASIL":^40}')
print(f'{"CENSO 2019":^40}')
print('-' * 40)

