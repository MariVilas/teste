negrito = '\033[1m'
limpa = '\033[m'
vermelho = '\033[31m'
amarelo = '\033[33m'
verde = '\033[32m'
azul = '\033[34m'

def titulo(msg):
    print('---'*10)
    print(f'{msg:^30}')
    print('---'*10)

def cadastro():
    titulo('CADASTRO')
    nome = str(input('Nome: '))
    idade = str(input('Idade: '))
    while True:
        if idade.isnumeric() == False:
            print(f'{vermelho}Digite um valor válido!{limpa}')
            idade = str(input('Idade: '))
        if idade.isnumeric() == True:
            break
    banco(nome, idade)
    print(f'{azul}PESSOA CADASTRADA COM SUCESSO!{limpa}')


def banco(nome, idade):
    arq = open('bancodedados.txt', 'a')
    arq.write(nome)
    arq.write(',')
    arq.write(idade)
    arq.write(',')
    arq.close()


def mostrar():
    arq = open('bancodedados.txt', 'r')
    l = []
    p = ''
    for c in arq.read():
        if c != ',':
            p += c
        elif c == ',':
            l.append(p[:])
            p = ''
    titulo('PESSOAS CADASTRADAS')
    for i, d in enumerate(l):
        if i % 2 == 0:
            print(f'{d:<20}', end='')
        elif i % 2 > 0:
            print(f'{d:>5} anos')


def menu():
    while True:
        titulo('MENU PRINCIPAL')
        print(f'{amarelo}1 -> {azul}Ver pessoas cadastradas{limpa}')
        print(f'{amarelo}2 -> {azul}Cadastrar nova pessoa{limpa}')
        print(f'{amarelo}3 -> {azul}Sair do Sistema{limpa}')
        print('---'*10)
        op = input(f'{amarelo}Digite uma opção: {limpa}')
        try:
            op = int(op)
        except:
            print(f'{vermelho}OPÇÃO INVÁLIDA!{limpa}')
        else:
            if op == 1:
                mostrar()
            elif op == 2:
                cadastro()
            elif op == 3:
                print(f'{vermelho}ENCERRANDO O SISTEMA...{limpa}')
                from time import sleep
                sleep(2)
                print('Obrigado e Volte Sempre!')
                break
            else:
                print(f'{vermelho}ERRO! Digite uma opção válida!{limpa}')
menu()