nota1= float(input('Digite a primeira nota: '))
nota2= float(input('Digite a segunda nota: '))
média = (nota1+nota2)/2
if média >= 6:
    print('Parabéns, sua média foi de {}! você passou'.format(média))
else:
    print('Você está de recuperação, sua média foi de {}!'.format(média))