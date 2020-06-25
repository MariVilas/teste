print('-'*30)
resp= 'S'
def linha():
    print('-=' * 20)
def ajuda(comando):
    help(comando)





while resp in 'Ss':
    linha()
    ajuda1 = str(input('\033[0;30;44mDigite o nome de uma função ou biblioteca: ')).strip().lower()
    ajuda(ajuda1)
    resp = str(input('\033[0;30;41mQuer continuar?[S/N]')).upper().strip()[0]
    linha()