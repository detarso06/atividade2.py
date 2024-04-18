conta= float(input('Número da sua conta:'))
saldo= float(input('Digite seu saldo: R$'))
debito= float(input('Digite seu débito: R$'))
credito= float(input('Digite seu crédito: R$'))
atual= saldo - (debito + credito)
if atual >= 0:
    print('Seu saldo atual é de R${}, ele é positivo!'.format(atual))
else:
    print('Seu saldo atual é de R${}, ele é negativo!'.format(atual))