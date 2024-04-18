maça= int(input('Quantas maças foram compradas: '))
if maça < 12:
    total= maça*1.3
    print('Você comprou {} maças. Valor de cada maça vale R$1,30. O total da compra é R${}'.format(maça,total))
else:
    total2= maça*1
    print('Você comprou {} maças. o valor de cada maça vale R$1,00. O total da compra é R${}'.format(maça,total2))