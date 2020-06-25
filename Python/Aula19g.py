import math
pessoa = dict()
idad = list()
mulher = list()
soma = media = 0
total= list()
while True:
    print('-' * 40)
    print(f'{"IBGE/BRASIL":^40}')
    print(f'{"CENSO 2019":^40}')
    print('-' * 40)
    pessoa['nome'] = str(input("Nome: "))
    pessoa['sexo'] = str(input("Sexo: [M/F] ")).strip().upper()[0]
    while pessoa['sexo'] not in "MF":
        pessoa['sexo'] = str(input("ERRO! Por favor, digite apenas M ou F ")).strip().upper()[0]
    if pessoa['sexo'] == "F":
        mulher.append(pessoa['nome'])
    pessoa['idade'] = int(input("Idade: "))
    soma += pessoa['idade']
    idad.append(pessoa.copy())
    total.append(pessoa.copy())
    resposta = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    while resposta not in "SN":
        resposta = str(input("ERRO! Responda apenas S ou N ")).strip().upper()[0]
    if resposta == "N":
        break
print("-=" * 30)
print(f"A) Ao todo foram cadastradas {len(total)} pessoas")
media = soma / len(idad)
print(f" B) A média de idade é de {media:5.2f} anos")
print(f" C) As mulheres cadastradas foram: {mulher}")
print(f" D) Lista das pessoas que estao acima da idade média e suas respectivas idades: ")
for p in idad:
    if p['idade'] >= media:
        print(f"{pessoa['nome']} = {pessoa['idade']}")
print("ENCERRADO")