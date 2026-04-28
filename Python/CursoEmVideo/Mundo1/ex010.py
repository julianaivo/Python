'''Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.'''

real = float(input('Quanto dinheiro você tem na carteira? R$'))

dolar = 3.27 #considere US$1.00 = R$3.27

total = real / dolar

print('Com R${:.2f} você pode comprar US${:.2f}'.format(real, total))
