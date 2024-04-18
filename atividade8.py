ea= int(input('Quantidade atual no estoque: '))
em= int(input('Quantidade máxima no estoque: '))
emi= int(input('Quantidade mínima no estoque: '))
media= (em + emi)/2
if ea >= media:
    print('Não efetuar a compra!')
else:
    print('Efetuar compra!')