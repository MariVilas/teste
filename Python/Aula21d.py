nome=[]
list = []
resp='S'
def linha():
    print('-=' * 20)
def maior():
        nome.append(str(input('Entre com o seu nome:')))
        list.append(int(input('Insira sua nota do 1º Bimestre: ')))
        list.append(int(input('Insira sua nota do 2º Bimestre: ')))
        list.append(int(input('Insira sua nota do 3º Bimestre: ')))
        list.append(int(input('Insira sua nota do 4º Bimestre: ')))
        m = max(list)
        m1= min(list)
        m2= sum(list)/len(list)
        if m2<5:
            print(f'Sua média final foi:{m2}  Reprovado')
        else:
            print(f'Sua média final foi:{m2}  Aprovado')
        print(f'A maior nota é: {m}\nA Menor nota é: {m1}')



def remover_matricula():
    del nome[0]
    del list[:]
    print('Aluno Removido')
    linha()
    linha()
    menu()


def menu():
    while True:
        print('-' * 40)
        print(f'{"Escola Fênix":^40}')
        print(f'{"Boletim Anual":^40}')
        print('-' * 40)
        print(f'1 -> Ver alunos cadastrados')
        print(f'2 -> Cadastrar novo aluno')
        print(f'3 -> Limpar o Sistema')
        print(f'4 -> Sair do Sistema')
        print('---'*10)
        op = input(f'Digite uma opção: ')
        try:
            op = int(op)
        except:
            print(f'OPÇÃO INVÁLIDA!')
        else:
            if op == 1:
                print(nome)
                print(list)
            elif op == 2:
                maior()
            elif op == 3:
                remover_matricula()
            elif op == 4:
                print(f'ENCERRANDO O SISTEMA...')
                from time import sleep
                sleep(2)
                print('Obrigado e Volte Sempre!')
                break



while resp in 'Ss':
    menu()
    resp = str(input('Quer continuar?[S/N]')).upper().strip()[0]
    print(f'ENCERRANDO O SISTEMA...')
    from time import sleep

    sleep(2)
    print('Obrigado e Volte Sempre!')
    break
    linha()
    linha()