num = int(input("digite um valor para calculo de PA: "))
razao = int(input("digite o valor da razao: "))
decimo = num + (10 - 1) * razao

c = num

while (c < decimo + razao):
    print("{} ".format(c), end="-> ")
    c = c + razao

print("ACABOU")