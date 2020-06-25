valor = int(input('Entre com o Valor da Imóvel:'))
salário=int(input('Entre com o valor da sua remuneração mensal:'))
tempo=int(input('Entre com a quantidade de parcelas que deseja efetuar o pagamento:'))
parcela= valor//tempo

if parcela <= salário*30/100:
  print('\033[4;31mFinanciamento Permitido!')
  print('\033[4;32mObrigada pela compra!')
else:
  print('\033[4;33mRenda insuficiente para o financiamento!')
  print('\033[4;32mProcure um outro imóvel!')


