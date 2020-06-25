sexo = str(input('Entre com o seu sexo:[M/F]')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados Inválidos, Tente Novamente:')).strip().upper()[0]
print('Sexo registrado com sucesso!',sexo)