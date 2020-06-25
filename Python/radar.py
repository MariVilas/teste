resp= 'S'
while resp in 'Ss':
    print('-' * 40)
    print(f'{"Radar do Zubiano":^40}')
    print(f'{"Cuidando das Estradas":^40}')
    print('---'*14)
    vel=int(input('Entre com a velocidade do veículo:'))
    if vel < 80:
     print('Parabéns, Motorista consciente e responsável!!!')
    elif vel > 80 and vel <90:
     print('Multa Média!!! Valor da Multa R$900')
    elif vel >90 and  vel <100:
     print('Multa Grave!!! Valor da Multa R$1200')
    elif vel >100:
     print('Multa Gravíssima!!! Valor da Multa R$2000')
    resp = str(input('Quer continuar?[S/N]')).upper().strip()[0]

print('-' * 40)
print('-' * 40)
print(f'ENCERRANDO O SISTEMA...')
print('-' * 40)
print('-' * 40)





