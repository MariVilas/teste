soma = 0
lista = ("À Vista", "Cartão à Vista", "Preço Fechado", "À Prazo")
resp= 'S'

while resp in 'Ss':
    for c in range(1,7):
         num=int(input('Digite o valor do produto: '.format(c)))
         soma = soma + num

    perguntar =int(input('''Escolha uma opção para sua compra:            
    
    [0] À Vista                                                            
    [1] Cartão à Vista                                                     
    [2] Preço Fechado                                                      
    {3} À Prazo                                                            
    
    Digite sua escolha: '''))


    v  = soma - (soma*10/100)
    c  = soma -(soma*5/100)
    p  = soma
    pz = soma+(soma*20/100)

    if perguntar == 0:
        print("Você tem 10% de desconto! O valor da sua compra é de:", v)
    elif perguntar == 1:
        print("Você tem 5% de desconto! O valor da sua compra é de:", c)
    elif perguntar == 2:
        print("Você paga o preço fechado! O valor da sua compra é de:", p)
    else:
        print("Você tem 20% de Acréscimo! O valor da sua compra é de:", pz)

    resp = str(input('Quer continuar?[S/N]')).upper().strip()[0]
    num
    print("-=" * 20)
    print("-=" * 20)
    print("-=" * 20)