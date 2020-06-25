resp= 'SN'
while True:
    print("-=" * 20)
    print("Seja bem-vindo ao banco do Zubiano!\n\n")
    print("-=" * 20)
    valor_saque = int(input("Digite o valor que você deseja sacar!\n Obs: Valor mínimo: R$10. Valor máximo: R$600.\n\n"))

    if valor_saque < 10 or valor_saque > 600:
        print("-=" * 20)
        print("não é possivel realizar o saque!")
    notas_receb100 = valor_saque // 100
    resto100 = valor_saque % 100
    notas_receb50 = resto100 // 50
    resto50 = resto100 % 50
    notas_receb10 = resto50 // 10
    resto10 = resto50 % 10
    notas_receb5 = resto10 // 5
    resto5 = resto10 % 5
    notas_receb1 = resto5
    resto1 = resto5 % 1

    if notas_receb100 != 0:
        if resto100 == 0:
            print(notas_receb100, "notas de R$ 100\n")
        if resto100 > 0:
            if resto50 == 0:
                print(notas_receb100, "notas de R$ 100\n", notas_receb50, "notas de R$ 50\n")
        if resto50 > 0 and resto10 == 0 and notas_receb50 != 0:
            print(notas_receb100, "notas de R$ 100\n", notas_receb50, "notas de R$ 50\n", notas_receb10, "notas de R$ 10\n")
        if resto50 > 0 and resto10 == 0 and notas_receb50 == 0:
            print(notas_receb100, "notas de R$ 100\n", notas_receb10, "notas de R$ 10\n")

        if resto10 > 0 and resto5 == 0 and notas_receb50 != 0 and notas_receb10 != 0:
            print(notas_receb100, "notas de R$ 100\n", notas_receb50, "notas de R$ 50\n", notas_receb10, "notas de R$ 10\n",
                  notas_receb5, "notas de R$ 5\n")
        if resto10 > 0 and resto5 == 0 and notas_receb50 == 0 and notas_receb10 != 0:
            print(notas_receb100, "notas de R$ 100\n", notas_receb10, "notas de R$ 10\n", notas_receb5, "notas de R$ 5\n")
        if resto10 > 0 and resto5 == 0 and notas_receb50 != 0 and notas_receb10 == 0:
            print(notas_receb100, "notas de R$ 100\n", notas_receb50, "notas de R$ 50\n", notas_receb5, "notas de R$ 5\n")
        if resto10 > 0 and resto5 == 0 and notas_receb50 == 0 and notas_receb10 == 0:
            print(notas_receb100, "notas de R$ 100\n", notas_receb5, "notas de R$ 5\n")

        if resto5 > 0 and notas_receb50 != 0 and notas_receb10 != 0 and notas_receb5 != 0:
            print(notas_receb100, "notas de R$ 100\n", notas_receb50, "notas de R$ 50\n", notas_receb10, "notas de R$ 10\n",
                  notas_receb5, "notas de R$ 5\n", notas_receb1, "notas de R$1\n")
        if resto5 > 0 and notas_receb50 == 0 and notas_receb10 != 0 and notas_receb5 != 0:
            print(notas_receb100, "notas de R$ 100\n", notas_receb10, "notas de R$ 10\n", notas_receb5, "notas de R$ 5\n",
                  notas_receb1, "notas de R$1\n")
        if resto5 > 0 and notas_receb50 != 0 and notas_receb10 == 0 and notas_receb5 != 0:
            print(notas_receb100, "notas de R$ 100\n", notas_receb50, "notas de R$ 50\n", notas_receb5, "notas de R$ 5\n",
                  notas_receb1, "notas de R$1\n")
        if resto5 > 0 and notas_receb50 != 0 and notas_receb10 != 0 and notas_receb5 == 0:
            print(notas_receb100, "notas de R$ 100\n", notas_receb50, "notas de R$ 50\n", notas_receb10, "notas de R$ 10\n",
                  notas_receb1, "notas de R$1\n")
        if resto5 > 0 and notas_receb50 == 0 and notas_receb10 == 0 and notas_receb5 != 0:
            print(notas_receb100, "notas de R$ 100\n", notas_receb5, "notas de R$ 5\n", notas_receb1, "notas de R$1\n")
        if resto5 > 0 and notas_receb50 == 0 and notas_receb10 != 0 and notas_receb5 == 0:
            print(notas_receb100, "notas de R$ 100\n", notas_receb10, "notas de R$ 10\n", notas_receb1, "notas de R$1\n")
        if resto5 > 0 and notas_receb50 != 0 and notas_receb10 == 0 and notas_receb5 == 0:
            print(notas_receb100, "notas de R$ 100\n", notas_receb50, "notas de R$ 50\n", notas_receb1, "notas de R$1\n")
        if resto5 > 0 and notas_receb50 == 0 and notas_receb10 == 0 and notas_receb5 == 0:
            print(notas_receb100, "notas de R$ 100\n", notas_receb1, "notas de R$1\n")

    if notas_receb100 == 0 and notas_receb50 != 0:
        if resto100 > 0:
            if resto50 == 0:
                print(notas_receb50, "notas de R$ 50\n")
        if resto50 > 0:
            if resto10 == 0:
                print(notas_receb50, "notas de R$ 50\n", notas_receb10, "notas de R$ 10\n")
        if resto10 > 0:
            if resto5 == 0:
                if notas_receb10 != 0:
                    print(notas_receb50, "notas de R$ 50\n", notas_receb10, "notas de R$ 10\n", notas_receb5,
                          "notas de R$ 5\n")
                else:
                    print(notas_receb50, "notas de R$ 50\n", notas_receb5, "notas de R$ 5\n")
        if resto5 > 0:
            if resto1 == 0 and notas_receb10 != 0 and notas_receb5 != 0:
                print(notas_receb50, "notas de R$ 50\n", notas_receb10, "notas de R$ 10\n", notas_receb5, "notas de R$ 5\n",
                      notas_receb1, "notas de R$1\n")
            if resto1 == 0 and notas_receb10 == 0 and notas_receb5 != 0:
                print(notas_receb50, "notas de R$ 50\n", notas_receb5, "notas de R$ 5\n", notas_receb1, "notas de R$1\n")
            else:
                print(notas_receb50, "notas de R$ 50\n", notas_receb1, "notas de R$1\n")

    if notas_receb100 == 0 and notas_receb50 == 0 and notas_receb10 != 0:
        if resto50 > 0:
            if resto10 == 0:
                print(notas_receb10, "notas de R$ 10\n")
        if resto10 > 0:
            if resto5 == 0:
                print(notas_receb10, "notas de R$ 10\n", notas_receb5, "notas de R$ 5\n")
        if resto5 > 0:
            if resto1 == 0:
                if notas_receb5 != 0:
                    print(notas_receb10, "notas de R$ 10\n", notas_receb5, "notas de R$ 5\n", notas_receb1,
                          "notas de R$1\n")
                else:
                    print(notas_receb10, "notas de R$ 10\n", notas_receb1, "notas de R$1\n")
    resp = str(input('Quer continuar?[S/N]')).upper().strip()[0]
    if resp == 'N':
        break
print("-=" * 20)
print("-=" * 20)
print("-=" * 20)
print('Obrigada por utilizar nossos serviços!!!')
print("-=" * 20)
print("-=" * 20)
print("-=" * 20)