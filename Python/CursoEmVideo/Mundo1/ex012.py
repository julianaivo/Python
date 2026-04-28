'''Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.'''

preco = float(input('Qual o preço do produto? R$'))

total = preco * 0.95  #(5% de desconto) 

print('O produto que custava R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f}.'.format(preco, total))